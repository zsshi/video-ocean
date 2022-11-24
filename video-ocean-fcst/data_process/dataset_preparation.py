import netCDF4 as nc
import numpy as np
import sys

fn = 'C:\\Users\\zsshi\\Desktop\\woa_temp_sani\\woa18_95A4_s00_01.nc'
# fn = 'C:\\Users\\zsshi\\Desktop\\woa_temp_sani\\woa18_95A4_s00_04.nc'
ds = nc.Dataset(fn)

print(ds)
print("++++++++++++++++++++++++++++++++++++++++++++++")
print("++++++++++++++++++++++++++++++++++++++++++++++")
print(ds.__dict__)
print("++++++++++++++++++++++++++++++++++++++++++++++")
print("++++++++++++++++++++++++++++++++++++++++++++++")
for dim in ds.dimensions.values():
    print(dim)
print("++++++++++++++++++++++++++++++++++++++++++++++")
print("++++++++++++++++++++++++++++++++++++++++++++++")
# print(ds.variables.keys())
for var in ds.variables.values():
    print(var)
# ['crs', 'lat', 'lat_bnds', 'lon', 'lon_bnds', 'depth', 'depth_bnds', 'time', 'climatology_bounds', 's_an', 's_mn', 's_dd', 's_sd', 's_se', 's_oa', 's_gp']
print("++++++++++++++++++++++++++++++++++++++++++++++")
print("++++++++++++++++++++++++++++++++++++++++++++++")
for key in ds.variables.keys():
    print(key + " - " + str(ds.variables[key].shape))

print(ds.variables["s_an"][:].nbytes / 1024.0 / 1024.0)

