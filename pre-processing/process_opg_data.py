""" 
Savanna Wolvin
Created: Mar 20th, 2024
Edited: Apr 22st, 2024


##### SUMMARY ################################################################
This script creates the facet data needed for the ciroh workshop.


"""
#%% Global variables

import cartopy.crs as ccrs
import cartopy.feature as cfeat
import cartopy.io.shapereader as shpreader
import matplotlib.pyplot as plt
import scipy.io as sio
import numpy as np
from matplotlib.colors import ListedColormap
from datetime import timedelta, datetime
import pandas as pd
from sklearn.linear_model import LinearRegression



#%% Variable locations

fi_dir = "/uufs/chpc.utah.edu/common/home/strong-group7/savanna/cstar/facets/"
opg_dir = "/uufs/chpc.utah.edu/common/home/strong-group7/savanna/cstar/opg/"
save_dir = "/uufs/chpc.utah.edu/common/home/strong-group7/savanna/cstar/facets/facet_figs/"

data_dir = "/uufs/chpc.utah.edu/common/home/strong-group7/savanna/ciroh_workshop/datasets/"

year_subset  = [1988, 2017]
month_subset = [12,1,2]

#%% load lats/lons/facets/orientation/opg/intercept

mat_file = sio.loadmat(fi_dir + 'lats')
lats  = np.array(mat_file['lats'])

mat_file = sio.loadmat(fi_dir + 'lons')
lons  = np.array(mat_file['lons'])

mat_file = sio.loadmat(fi_dir + 'facets_labeled')
facets  = mat_file['facets_i'].astype('float')

mat_file = sio.loadmat(fi_dir + 'facets')
orientation  = np.array(mat_file['facets']).astype('float')

mat_file = sio.loadmat(opg_dir + 'all_opg')  
opgs = mat_file['allOPG_qc2']

mat_file = sio.loadmat(fi_dir + 'elev')
elev  = np.array(mat_file['elev'])

mat_file = sio.loadmat(opg_dir + 'newtest_2stn_opg_int_20')
y_int = mat_file['allOPGint']


#%% data for Northern Utah Facets

mat_file = sio.loadmat(opg_dir + 'prcp_latlon_15629')
mesonet  = np.array(mat_file['prcp_latlon_15629'])

mat_file = sio.loadmat(fi_dir + 'station_facet_assignment')
station_facet  = np.array(mat_file['station_facet'])

mat_file = sio.loadmat(opg_dir + 'prcpout_15629')
prcpout_15629  = np.array(mat_file['prcpout_15629'][:,3:])


#%% Subset the data by the area - NORTHERN UTAH

# determine facets in the northern utah area
norUT = np.unique(facets[239:312, 382:503])

# remove facets outside of northern utah
for fi in np.unique(facets):
    if fi not in norUT:
        orientation[facets == fi] = np.nan
        facets[facets == fi] = np.nan
        
# subset to the area these facets take up
lats        = lats[209:331, 350:557]
lons        = lons[209:331, 350:557]
facets      = facets[209:331, 350:557]
orientation = orientation[209:331, 350:557]
elev        = elev[209:331, 350:557]

# subset to the facets 
opgs  = opgs[:, norUT.astype('int')-1]
y_int = y_int[:, norUT.astype('int')-1]



#%% create pandas dataframe with dates and opgs

time_ref    = np.arange(datetime(1979, 1, 1), datetime(2018, 4, 1), 
                            timedelta(days=1), dtype='object')

# Here we have winter opgs from northern utah facets
opgDF = pd.DataFrame(data=opgs, index=time_ref, columns=norUT.astype('int')) # create dataframe
opgDF = opgDF.loc[opgDF.index.month.isin(month_subset), :] # subset to winter
opgDF = opgDF.loc[opgDF.index.year.isin(np.arange(year_subset[0], year_subset[1]+1).astype('int')), :] # subset to years desired
opgDF = opgDF.dropna(axis=1, how='all') # subset to facets with observations

# Here we have winter y-intercepts from northern utah facets
y_intDF = pd.DataFrame(data=y_int, index=time_ref, columns=norUT.astype('int')) # create dataframe
y_intDF = y_intDF.loc[y_intDF.index.month.isin(month_subset), :] # subset to winter
y_intDF = y_intDF.loc[y_intDF.index.year.isin(np.arange(year_subset[0], year_subset[1]+1).astype('int')), :] # subset to years desired
y_intDF = y_intDF.dropna(axis=1, how='all') # subset to facets with observations
y_intDF = y_intDF.loc[:, y_intDF.columns.isin(opgDF.columns)]


# here we subset the orientation and facet numbers of the map
norUT = opgDF.columns
for fi in np.unique(facets):
    if fi not in norUT:
        orientation[facets == fi] = np.nan
        facets[facets == fi] = np.nan

# Subset the observational precipitation to the correct facets
idx       = np.squeeze(np.isin(station_facet, norUT.astype('int')-1))
prcp_meso = prcpout_15629[:, idx]
mesonet   = mesonet[idx, :]
stations  = np.squeeze(station_facet[idx, :])

# Here we have winter precipitation from northern utah facets
prcpDF = pd.DataFrame(data=prcp_meso, index=time_ref, columns=stations) # create dataframe
prcpDF = prcpDF.loc[prcpDF.index.month.isin(month_subset), :] # subset to winter
prcpDF = prcpDF.loc[prcpDF.index.year.isin(np.arange(year_subset[0], year_subset[1]+1).astype('int')), :] # subset to years desired

# Here we have winter station locations from northern utah facets
msntDF = pd.DataFrame(data=mesonet, index=stations, columns=['latitude','longitude']) # create dataframe



#%% Formulate the correlation between the OPG and y-intercept of each facet

linear_coef = np.zeros((3, np.shape(opgDF)[1]))

# fit each feact and save to an array
for fi in range(len(opgDF.columns)):
    # pull x and y values
    x = opgDF.iloc[:,fi].values.reshape(-1, 1)
    y = y_intDF.iloc[:,fi].values.reshape(-1, 1)
    
    # index nans
    idx = np.isnan(x)
    
    # fit linear regression
    model = LinearRegression().fit(x[~idx].reshape(-1, 1), y[~idx].reshape(-1, 1))

    # save values
    linear_coef[0, fi] = model.coef_
    linear_coef[1, fi] = model.intercept_
    linear_coef[2, fi] = (np.corrcoef(x[~idx], y[~idx])[0,1])**2


linear_coef = pd.DataFrame(data=linear_coef, index=['coef','intercept','score'], columns=opgDF.columns)
        
        
#%% save datasets

opgDF.to_csv(f"{data_dir}winter_northernUT_opg.csv")
y_intDF.to_csv(f"{data_dir}winter_northernUT_y_intrcpt.csv")
linear_coef.to_csv(f"{data_dir}winter_northernUT_lin_model_opg_y-int.csv")
prcpDF.to_csv(f"{data_dir}winter_northernUT_precip_obs.csv")
msntDF.to_csv(f"{data_dir}winter_northernUT_precip_obs_latlon.csv")
pd.DataFrame(lats).to_csv(f"{data_dir}lats.csv")
pd.DataFrame(lons).to_csv(f"{data_dir}lons.csv")
pd.DataFrame(facets).to_csv(f"{data_dir}facet_labels.csv")
pd.DataFrame(orientation).to_csv(f"{data_dir}facet_orientation.csv")
pd.DataFrame(elev).to_csv(f"{data_dir}elevation.csv")


#%% Plot the Facet's Orientation without Flat
print("Plot Figure #2...")

cmap_fi2 = ListedColormap([[0.0, 0.0, 0.0],[0.1428, 0.1428, 0.1428],[0.2857, 0.2857, 0.2857],
           [0.4285, 0.4285, 0.4285],[0.5714, 0.5714, 0.5714],[0.7142, 0.7142, 0.7142],
           [0.8571, 0.8571, 0.8571],[1.0, 1.0, 1.0]])

# Preset Values
extent = [-119, -106, 36, 45]
datacrs = ccrs.PlateCarree()

# Create Figure
fig = plt.figure( figsize = (10, 6))
ax = fig.add_axes( [0.1, 0.1, 0.8, 0.8], projection = ccrs.Mercator(central_longitude=np.mean(lons)) )

# Add Facets
orientx = orientation.astype('float')
orientx[orientx == 9] = np.nan
pcm = ax.pcolormesh(lons, lats, orientx, cmap=cmap_fi2, transform=datacrs, shading='auto')
pcm.set_clim(0.5,8.5)

# add labels
# for fi in range(np.min(facets), np.max(facets)+1):
#     fi_lon = np.median(lons[facets==fi])
#     fi_lat = np.median(lats[facets==fi])
#     plt.text(fi_lon, fi_lat, str(fi), fontsize = 1, color = 'midnightblue', 
#              transform = datacrs, ha = 'center', va = 'center', 
#              bbox=dict(boxstyle="round", fc=(1,1,1), linewidth=0.1))


# Cartography
ax.add_feature(cfeat.LAND, facecolor="burlywood")
ax.add_feature(cfeat.STATES.with_scale('10m'), edgecolor="saddlebrown")
ax.set_extent(extent)

# Add colorbar
cbar = plt.colorbar(pcm, ticks=[0,1,2,3,4,5,6,7,8,9])
cbar.set_label("Orientation", fontsize=14)
cbar.ax.set_yticklabels(['','WSW','SSW','SSE','ESE','ENE','NNE','NNW','WNW',''])
cbar.ax.tick_params(labelsize=14)

# Save and Show Figure
# print("Save Figure...")
# plt.savefig(save_dir + "facet_orientation2_labeled.png", dpi=1250, transparent=True, \
#             bbox_inches='tight')

plt.show()









