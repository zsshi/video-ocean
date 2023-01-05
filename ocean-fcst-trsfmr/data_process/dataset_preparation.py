import netCDF4 as nc
import numpy as np
import numpy.ma as ma
import sys

import h5py

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# fn = 'C:\\Users\\zsshi\\Desktop\\woa_temp_sani\\woa18_95A4_s00_01.nc'
# fn = 'C:\\Users\\zsshi\\Desktop\\woa_temp_sani\\woa18_95A4_t00_04.nc'
# fn = 'C:\\Users\\zsshi\\Desktop\\woa_temp_sani\\hycom_GLBv0.08_539_2015010112_t000.nc'
# fn = 'C:\\Users\\zsshi\\Desktop\\woa_temp_sani\\hycom-lat_00_45-lon_90_180-r024-19960103.nc4'
fn = 'C:\\Users\\zsshi\\Desktop\\woa_temp_sani\\data_1996.nc4'
# fn = 'C:\\Users\\zsshi\\Desktop\\woa_temp_sani\\sst-day-mean-ltm-1991-2020.nc'
ds = nc.Dataset(fn)

print(ds)
# print("++++++++++++++++++++++++++++++++++++++++++++++")
# print("++++++++++++++++++++++++++++++++++++++++++++++")
print(ds.__dict__)
# print("++++++++++++++++++++++++++++++++++++++++++++++")
# print("++++++++++++++++++++++++++++++++++++++++++++++")
for dim in ds.dimensions.values():
    print(dim)
# print("++++++++++++++++++++++++++++++++++++++++++++++")
# print("++++++++++++++++++++++++++++++++++++++++++++++")
print(ds.variables.keys())

for key in ds.variables.keys():
    print(key + " - " + str(ds.variables[key].shape))
    # print(type(ds.variables[key][:]))
    # print(str(ds.variables[key][:].shape))
    # print(str(ds.variables[key][:].view(ma.MaskedArray)))

time = ds.variables['time'][:]
lat = ds.variables['lat'][:]
lon = ds.variables['lon'][:]

print(time)
print(lat)
print(lon)

# OISST
# dict_keys(['lat', 'lon', 'time', 'climatology_bounds', 'sst', 'valid_yr_count'])
# sst = ds.variables["sst"][:]
# print(sst.shape)
# print(sst.count())
# print(sst.compressed().shape)
# print(sst[0,:].min())
# print(sst[0,:].max())

# WOA
# ['crs', 'lat', 'lat_bnds', 'lon', 'lon_bnds', 'depth', 'depth_bnds', 'time', 'climatology_bounds', 's_an', 's_mn', 's_dd', 's_sd', 's_se', 's_oa', 's_gp']
# depth = ds.variables['depth'][:]
# t_an = ds.variables['t_an'][:]
# for i in range(len(depth)):
#     print("{}:{}".format(depth[i], t_an[0,:,360,100][i]))

# HyCOM
# dict_keys(['time', 'tau', 'depth', 'lat', 'lon', 'water_u', 'water_u_bottom', 'water_v', 'water_v_bottom', 'water_temp', 'water_temp_bottom', 'salinity', 'salinity_bottom', 'surf_el'])

# tau = ds.variables['tau'][:]
depth = ds.variables['depth'][:]
# water_temp = ds.variables['water_temp'][:]
# for i in range(len(depth)):
#     print("{}:{}".format(depth[i], water_temp[0,:,1200,100][i]))
# salinity = ds.variables['salinity'][:]
# for i in range(len(depth)):
#     print("{}:{}".format(depth[i], salinity[0,:,1200,100][i]))
water_u = ds.variables['water_u'][:]
# for i in range(len(depth)):
#     print("{}:{}".format(depth[i], water_u[0,:,1200,100][i]))
# water_v = ds.variables['water_v'][:]
# for i in range(len(depth)):
#     print("{}:{}".format(depth[i], water_v[0,:,1200,100][i]))

# world
# m = Basemap(projection='cyl',llcrnrlat=-90,urcrnrlat=90,\
#             llcrnrlon=-180,urcrnrlon=180,resolution='c')
# china
# m = Basemap(projection='cyl',llcrnrlat=3,urcrnrlat=54,\
#             llcrnrlon=73,urcrnrlon=136,resolution='c')

# water_u = ds.variables["water_u"][:]
# print(water_u.shape)
# print(water_u.count())
# print(water_u.compressed().shape)
# print(water_u.compressed()[1000:1100])

# water_u_bottom = ds.variables["water_u_bottom"][:]
# print(water_u_bottom.shape)
# print(water_u_bottom.count())
# print(water_u_bottom.compressed().shape)
