# import netCDF4 as nc
import numpy as np
import numpy.ma as ma

import os
import sys

# import h5py
import datetime
import subprocess

import matplotlib.pyplot as plt
# from mpl_toolkits.basemap import Basemap

# base_url = "http://ncss.hycom.org/thredds/ncss/GLBv0.08/expt_53.X/data/1994?var=salinity_bottom&var=surf_el&var=water_temp_bottom&var=water_u_bottom&var=water_v_bottom&var=salinity&var=water_temp&var=water_u&var=water_v&north=45&west=90&east=180&south=0&disableProjSubset=on&horizStride=3&time_start=1994-01-01T12%3A00%3A00Z&time_end=1994-01-03T12%3A00%3A00Z&timeStride=2&vertStride=1&addLatLon=true&accept=netcdf4"

# base_url = "http://ncss.hycom.org/thredds/ncss/GLBv0.08/expt_53.X/data/1994?var=salinity_bottom&var=surf_el&var=water_temp_bottom&var=water_u_bottom&var=water_v_bottom&var=salinity&var=water_temp&var=water_u&var=water_v&north=24.78&west=98.4&east=124.4&south=3.99&disableProjSubset=on&horizStride=1&time_start=1994-01-01T12%3A00%3A00Z&time_end=1994-01-03T09%3A00%3A00Z&timeStride=1&vertStride=1&addLatLon=true&accept=netcdf4"

def create_assist_date(datestart = None, dateend = None):
    if datestart is None:
        datestart = '2016-01-01'
    if dateend is None:
        dateend = datetime.datetime.now().strftime('%Y-%m-%d')
    
    datestart=datetime.datetime.strptime(datestart,'%Y-%m-%d')
    dateend=datetime.datetime.strptime(dateend,'%Y-%m-%d')
    date_list = []
    date_list.append(datestart.strftime('%Y-%m-%d'))
    while datestart < dateend:
        datestart += datetime.timedelta(days =+ 1)
        date_list.append(datestart.strftime('%Y-%m-%d'))
    return date_list

start_year = sys.argv[1]
end_year = sys.argv[2]
# start_year = 1995
# end_year = 1995

start_date = "{}-01-01".format(start_year)
end_date = "{}-12-31".format(end_year)

date_list = create_assist_date(start_date, end_date)
# hour_list = ["12", "18", "00", "06"] # start from 12
# print(len(date_list))
# print(date_list)

for i in range(len(date_list)):
    year = date_list[i][0:4]
    cur_date = date_list[i]
    next_date = date_list[i+1] if i != (len(date_list)-1) else cur_date
    base_url = "\"http://ncss.hycom.org/thredds/ncss/GLBv0.08/expt_53.X/data/{}?var=salinity_bottom&var=surf_el&var=water_temp_bottom&var=water_u_bottom&var=water_v_bottom&var=salinity&var=water_temp&var=water_u&var=water_v&north=45&west=90&east=180&south=0&disableProjSubset=on&horizStride=3&time_start={}T12%3A00%3A00Z&time_end={}T09%3A00%3A00Z&timeStride=2&vertStride=1&addLatLon=true&accept=netcdf4\"".format(year, cur_date, next_date)
    nc_file_name = "hycom-lat_00_45-lon_90_180-r024-{}.nc4".format(cur_date.replace("-",""))
    print(base_url)
    print(nc_file_name)
    if not os.path.exists(nc_file_name):
        # cmd = "aria2c -s 8 -c {} -o {}".format(base_url, nc_file_name)
        # cmd = "aria2c {} -o {}".format(base_url, nc_file_name)
        cmd = "curl {} -o {}".format(base_url, nc_file_name)
        subprocess.call(cmd, shell=True)
    else:
        print("{} is existing, skipping......".format(nc_file_name))
exit()

# below is netcdf processing.
fn = 'C:\\Users\\zsshi\\Desktop\\woa_temp_sani\\hycom_GLBv0.08_539_2015010112_t000.nc'
h5_file = 'C:\\Users\\zsshi\\Desktop\\woa_temp_sani\\hycom_example.h5'

ds = nc.Dataset(fn)
print(ds)
print(ds.__dict__)
for dim in ds.dimensions.values():
    print(dim)
print(ds.variables.keys())

for key in ds.variables.keys():
    print(key + " - " + str(ds.variables[key].shape))

time = ds.variables['time'][:]
tau = ds.variables['tau'][:]
depth = ds.variables['depth'][:]
lat = ds.variables['lat'][:]
lon = ds.variables['lon'][:]

# del_lat_index = np.where((lat < 0.0) | (lat >= 60.0))
# del_lon_index = np.where(lon < 90.0)
# print(del_lat_index)
# print(del_lat_index[0].shape)
# print(del_lon_index)
# print(del_lon_index[0].shape)

# South China Sea
lat_index_save = np.where((lat >= 3.99) & (lat <= 24.78))
lon_index_save = np.where((lon >= 98.4) & (lon <= 124.4))

# East Asia
# lat_index_save = np.where((lat >= 0.0) & (lat < 60.0))
# lon_index_save = np.where(lon >= 90.0)

lat_save = lat[lat_index_save[0]]
lon_save = lon[lon_index_save[0]]

water_u_save = ds.variables['water_u'][:,:,lat_index_save[0],lon_index_save[0]]
water_u_bottom_save = ds.variables['water_u_bottom'][:,lat_index_save[0],lon_index_save[0]]
water_v_save = ds.variables['water_v'][:,:,lat_index_save[0],lon_index_save[0]]
water_v_bottom_save = ds.variables['water_v_bottom'][:,lat_index_save[0],lon_index_save[0]]
water_temp_save = ds.variables['water_temp'][:,:,lat_index_save[0],lon_index_save[0]]
water_temp_bottom_save = ds.variables['water_temp_bottom'][:,lat_index_save[0],lon_index_save[0]]
salinity_save = ds.variables['salinity'][:,:,lat_index_save[0],lon_index_save[0]]
salinity_bottom_save = ds.variables['salinity_bottom'][:,lat_index_save[0],lon_index_save[0]]
surf_el_save = ds.variables['surf_el'][:,lat_index_save[0],lon_index_save[0]]

f_h5 = h5py.File(h5_file, "w")
g1 = f_h5.create_group("g1")
g1.create_dataset("time", data=time, compression="gzip")
g1.create_dataset("tau", data=tau, compression="gzip")
g1.create_dataset("depth", data=depth, compression="gzip")
g1.create_dataset("lat", data=lat_save, compression="gzip")
g1.create_dataset("lon", data=lon_save, compression="gzip")

g1.create_dataset("water_u", data=water_u_save, compression="gzip")
g1.create_dataset("water_u_bottom", data=water_u_bottom_save, compression="gzip")
# g1.create_dataset("water_v", data=water_v_save, compression="gzip")
# g1.create_dataset("water_v_bottom", data=water_v_bottom_save, compression="gzip")
# g1.create_dataset("water_temp", data=water_temp_save, compression="gzip")
# g1.create_dataset("water_temp_bottom", data=water_temp_bottom_save, compression="gzip")
# g1.create_dataset("salinity", data=salinity_save, compression="gzip")
# g1.create_dataset("salinity_bottom", data=salinity_bottom_save, compression="gzip")
# g1.create_dataset("surf_el", data=surf_el_save, compression="gzip")

print("+++++++++++++++++++++++++++++++++++++++")
print("New hdf5 file......")

for key in f_h5["g1"].keys():
    print(key + " - " + str(f_h5["g1"][key].shape))

f_h5.close()

# nc_file_save = 'C:\\Users\\zsshi\\Desktop\\woa_temp_sani\\netcdf_example.nc'
# ncfile = nc.Dataset(nc_file_save, mode='w', format='NETCDF4_CLASSIC')

# ncfile.createDimension('time', 1)
# ncfile.createDimension('tau', 1)
# ncfile.createDimension('depth', 40)
# ncfile.createDimension('lat', 1000)
# ncfile.createDimension('lon', 1125)

# ncfile.createVariable('time', np.float32, ('time',), zlib=True)
# ncfile.createVariable('tau', np.float32, ('tau',), zlib=True)
# ncfile.createVariable('depth', np.float32, ('depth',), zlib=True)
# ncfile.createVariable('lat', np.float32, ('lat',), zlib=True)
# ncfile.createVariable('lon', np.float32, ('lon',), zlib=True)
# ncfile.createVariable('water_u', np.float32, ('time', 'depth', 'lat', 'lon'), zlib=True)
# ncfile.createVariable('water_u_bottom', np.float32, ('time', 'lat', 'lon'), zlib=True)
# ncfile.createVariable('water_v', np.float32, ('time', 'depth', 'lat', 'lon'), zlib=True)
# ncfile.createVariable('water_v_bottom', np.float32, ('time', 'lat', 'lon'), zlib=True)
# ncfile.createVariable('water_temp', np.float32, ('time', 'depth', 'lat', 'lon'), zlib=True)
# ncfile.createVariable('water_temp_bottom', np.float32, ('time', 'lat', 'lon'), zlib=True)
# ncfile.createVariable('salinity', np.float32, ('time', 'depth', 'lat', 'lon'), zlib=True)
# ncfile.createVariable('salinity_bottom', np.float32, ('time', 'lat', 'lon'), zlib=True)
# ncfile.createVariable('surf_el', np.float32, ('time', 'lat', 'lon'), zlib=True)

# ncfile.variables['time'][:] = time
# ncfile.variables['tau'][:] = tau
# ncfile.variables['depth'][:] = depth
# ncfile.variables['lat'][:] = lat_save
# ncfile.variables['lon'][:] = lon_save
# ncfile.variables['water_u'][:] = water_u_save
# ncfile.variables['water_u_bottom'][:] = water_u_bottom_save
# ncfile.variables['water_v'][:] = water_v_save
# ncfile.variables['water_v_bottom'][:] = water_v_bottom_save
# ncfile.variables['water_temp'][:] = water_temp_save
# ncfile.variables['water_temp_bottom'][:] = water_temp_bottom_save
# ncfile.variables['salinity'][:] = salinity_save
# ncfile.variables['salinity_bottom'][:] = salinity_bottom_save
# ncfile.variables['surf_el'][:] = surf_el_save

# ncfile.close()
