""" 
Savanna Wolvin
Created: Mar 21th, 2024
Edited: Mar 21st, 2024


##### SUMMARY ################################################################
This script creates the atmospheric data needed for the ciroh workshop.


"""
#%% Global imports

import xarray as xr
import numpy as np
from datetime import timedelta, datetime
from tqdm import tqdm



#%% Variable Presets

d_dir = "/uufs/chpc.utah.edu/common/home/strong-group7/" + \
    "savanna/ecmwf_era5/"
    
data_dir = "/uufs/chpc.utah.edu/common/home/strong-group7/savanna/ciroh_workshop/datasets/"

d_types      = {"uwnd": ["700"],
                    "vwnd": ["700"],
                    "hgt": ["500"],
                    "IVT": ["sfc"],
                    "precip": ["sfc"],
                    "shum": ["700"],
                    "temp": ["700"]}

year_subset  = [1988, 2017]
month_subset = [12,1,2]
lat_subset   = [36, 45]
lon_subset   = [-119, -106]


#%%

# Create Array of All Desired Years
d_years = np.arange(year_subset[0], year_subset[1]+1).astype('int')

# Create Array of All Desired Days
d_days = np.arange(datetime(year_subset[0],1,1), datetime(year_subset[1],3,1), timedelta(days=1)).astype(datetime)
d_days = np.array([i for i in d_days if i.month in month_subset]).astype('datetime64[ns]')

# Create Latitude and Longitude Arrays
d_lats = np.arange(lat_subset[0], lat_subset[1]+0.5, 0.5)
d_lons = np.arange(lon_subset[0], lon_subset[1]+0.5, 0.5)


#%% loop through the data vars, subset to year and area, and save the netcdfs

for atmos_varsX in d_types:
    pressure_levels = d_types[atmos_varsX]
    
    for press_levX in pressure_levels:
        atmosphereX = xr.Dataset()
        
        if press_levX == "sfc":
            for data_yearsX in tqdm(d_years, desc=atmos_varsX+" "+press_levX): # loop through each year 
            
                # Create Array of All Desired Days
                d_days = np.arange(datetime(data_yearsX,1,1), datetime(data_yearsX+1,1,1), timedelta(days=1)).astype(datetime)
                d_days = np.array([i for i in d_days if i.month in month_subset]).astype('datetime64[ns]')
            
                # Access the NC File and Convert Dataset to an Xarray
                ncfile = xr.open_dataset(
                    d_dir + "daily/sfc/era5_" + atmos_varsX + "_" + str(data_yearsX) + "_oct-apr_daily.nc")
                
                # Index the Pressure Lats, Lons, and Time of the NCfile
                ncfile = ncfile.sel(latitude=d_lats, longitude=d_lons, 
                                    time=d_days)     
                
                # reorder 
                
                # Save Atmospheric Variable
                atmosphereX = xr.merge([atmosphereX, ncfile])
            
            
        else:
            for data_yearsX in tqdm(d_years, desc=atmos_varsX+" "+press_levX): # loop through each year    
                
                # Create Array of All Desired Days
                d_days = np.arange(datetime(data_yearsX,1,1), datetime(data_yearsX+1,1,1), timedelta(days=1)).astype(datetime)
                d_days = np.array([i for i in d_days if i.month in month_subset]).astype('datetime64[ns]')
            
            
                # Access the NC File and Convert Dataset to an Xarray
                ncfile = xr.open_dataset(
                    d_dir + "daily/press/era5_" + atmos_varsX + "_" + str(data_yearsX) + "_oct-apr_daily.nc")
            
                # Index the Pressure Level, Lats, Lons, and Time of the NCfile
                ncfile = ncfile.sel(level=int(press_levX), 
                                    latitude=d_lats, longitude=d_lons, 
                                    time=d_days)
                
                # Save Atmospheric Variable
                atmosphereX = xr.merge([atmosphereX, ncfile])
                
        atmosphereX.to_netcdf(f"{data_dir}{atmos_varsX}_{press_levX}.nc")
        
        print(atmosphereX)
            
    
