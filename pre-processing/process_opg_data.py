""" 
Savanna Wolvin
Created: Mar 20th, 2024
Edited: Mar 21st, 2024


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



#%% Variable locations

fi_dir = "/uufs/chpc.utah.edu/common/home/strong-group7/savanna/cstar/facets/"
opg_dir = "/uufs/chpc.utah.edu/common/home/strong-group7/savanna/cstar/opg/"
save_dir = "/uufs/chpc.utah.edu/common/home/strong-group7/savanna/cstar/facets/facet_figs/"

data_dir = "/uufs/chpc.utah.edu/common/home/strong-group7/savanna/ciroh_workshop/datasets/"

year_subset  = [1988, 2017]
month_subset = [12,1,2]

#%% load lats/lons/facets/orientation/opg

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


#%% Subset the data by the area - NORTHERN UTAH

# determine facets in the northern utah area
norUT = np.unique(facets[239:312, 382:503])

# remove facets outside of northern utah
for fi in np.unique(facets):
    if fi not in norUT:
        orientation[facets == fi] = np.nan
        facets[facets == fi] = np.nan
        
# subset to the area these facets take up
lats = lats[209:331, 350:557]
lons = lons[209:331, 350:557]
facets = facets[209:331, 350:557]
orientation = orientation[209:331, 350:557]
opgs = opgs[:, norUT.astype('int')-1]


#%% create pandas dataframe with dates and opgs

time_ref    = np.arange(datetime(1979, 1, 1), datetime(2018, 4, 1), 
                            timedelta(days=1), dtype='object')

opgDF = pd.DataFrame(data=opgs, index=time_ref, columns=norUT.astype('int')) # create dataframe
opgDF = opgDF.loc[opgDF.index.month.isin(month_subset), :] # subset to winter
opgDF = opgDF.loc[opgDF.index.year.isin(np.arange(year_subset[0], year_subset[1]+1).astype('int')), :] # subset to years desired
opgDF = opgDF.dropna(axis=1, how='all') # subset to facets with observations

# now we have winter opgs from northern utah facets

# here we subset the orientation and facet numbers of the map
norUT = opgDF.columns
for fi in np.unique(facets):
    if fi not in norUT:
        orientation[facets == fi] = np.nan
        facets[facets == fi] = np.nan
        
        
#%% save datasets

opgDF.to_csv(f"{data_dir}winter_northernUT_opg.csv")
pd.DataFrame(lats).to_csv(f"{data_dir}lats.csv")
pd.DataFrame(lons).to_csv(f"{data_dir}lons.csv")
pd.DataFrame(facets).to_csv(f"{data_dir}facet_labels.csv")
pd.DataFrame(orientation).to_csv(f"{data_dir}facet_orientation.csv")


#%% load in the small scale features

# reader = shpreader.Reader('countyl010g.shp')
# counties = list(reader.geometries())
# COUNTIES = cfeature.ShapelyFeature(counties, ccrs.PlateCarree())



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









