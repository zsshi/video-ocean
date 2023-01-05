from mpl_toolkits.basemap import Basemap
from netCDF4 import Dataset, date2index
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
date = datetime(2007,12,15,0) # date to plot.

# open dataset.
# dataset = \
# Dataset('http://www.ncdc.noaa.gov/thredds/dodsC/OISST-V2-AVHRR_agg')
# fn = 'C:\\Users\\zsshi\\Desktop\\woa_temp_sani\\sst-day-mean-ltm-1991-2020.nc'
fn = 'C:\\Users\\zsshi\\Desktop\\woa_temp_sani\\hycom_GLBv0.08_539_2015010112_t000.nc'
# fn = 'C:\\Users\\zsshi\\Desktop\\woa_temp_sani\\woa18_95A4_t00_04.nc'
dataset = Dataset(fn)
timevar = dataset.variables['time']
timeindex = 0
# timeindex = date2index(date,timevar) # find time index for desired date.
# read sst.  Will automatically create a masked array using
# missing_value variable attribute. 'squeeze out' singleton dimensions.
# sst = dataset.variables['sst'][timeindex,:].squeeze()
# sst = dataset.variables['t_an'][timeindex,timeindex,:].squeeze()
sst = dataset.variables['water_temp'][timeindex,timeindex,:].squeeze()
# read ice.
# ice = dataset.variables['sst'][timeindex,:].squeeze()
# read lats and lons (representing centers of grid boxes).
lats = dataset.variables['lat'][:]
lons = dataset.variables['lon'][:]
lons, lats = np.meshgrid(lons,lats)
# create figure, axes instances.
fig = plt.figure()
ax = fig.add_axes([0.05,0.05,0.9,0.9])
# create Basemap instance.
# coastlines not used, so resolution set to None to skip
# continent processing (this speeds things up a bit)
# m = Basemap(projection='kav7',lon_0=0,resolution=None)
m = Basemap(projection='cyl',llcrnrlat=0,urcrnrlat=60,\
            llcrnrlon=90,urcrnrlon=180,resolution='c')
# draw line around map projection limb.
# color background of map projection region.
# missing values over land will show up this color.
m.drawmapboundary(fill_color='0.3')
# plot sst, then ice with pcolor
im1 = m.pcolormesh(lons,lats,sst,shading='flat',cmap=plt.cm.jet,latlon=True)
# im2 = m.pcolormesh(lons,lats,ice,shading='flat',cmap=plt.cm.gist_gray,latlon=True)
# draw parallels and meridians, but don't bother labelling them.
# m.drawparallels(np.arange(-90.,99.,30.))
# m.drawmeridians(np.arange(-180.,180.,60.))
m.drawparallels(np.arange(0.,60.,10.))
m.drawmeridians(np.arange(90.,180.,15.))
# add colorbar
cb = m.colorbar(im1,"bottom", size="5%", pad="2%")
# add a title.
ax.set_title('SST and ICE analysis for %s'%date)
plt.savefig("C:\\Users\\zsshi\\Desktop\\woa_temp_sani\\plot.jpg")
plt.show()