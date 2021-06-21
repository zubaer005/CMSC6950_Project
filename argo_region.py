
from mpl_toolkits.basemap import Basemap

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import argopy
import matplotlib.colors as colors

##Import argo data loader

from argopy import DataFetcher as ArgoDataFetcher
argo_loader = ArgoDataFetcher()

fig = plt.figure(figsize=(6,7)) 

# Initializing basemap
m = Basemap(projection='lcc', resolution='h', lat_0=43, lon_0=145, width=2E6, height=3E6)
m.shadedrelief()
m.drawcoastlines(color='gray')
m.drawcountries(color='gray')


#Load Argo data from a specific region and over a certain time frame into an x.array.Dataset

#ds_points = argo_loader.region([-75, -55, 30, 40, 0, 100, '2011-01-01', '2012-12-31']).to_xarray()
ds_points = argo_loader.region([140, 150, 35, 50, 0, 100, '2015-06-01', '2015-12-30']).to_xarray()
#Create a pandas dataframe and export to a csv file

df = ds_points.to_dataframe()
df.to_csv (r'task1.csv', index = False, header=True)  #Export data frame to a csv file

 

 
# Steps taken to convert ds_points which are in the form of xarray.
# For more information refer to the final report.
ds = ds_points.argo.point2profile()
df = ds.to_dataframe()
df = df.reset_index()

# Only keeping the useful columns for the purposes of this projection
df = df[['LATITUDE','LONGITUDE']]

# Preparing data for basemap
x,y = m(df['LONGITUDE'], df['LATITUDE'])

# Plotting the hexbin. More information in the report.
thiscmap = plt.cm.get_cmap('viridis')
m.hexbin(x, y, gridsize=[6,6], mincnt=1, cmap='summer', norm=colors.LogNorm(), alpha=0.4) 
cbar = plt.colorbar() 
cbar.ax.set_ylabel('# of argo reports', rotation=270, fontsize = 12)

# Indication certain locations on the map
lats = [43.0618,35.6762,38.2682,44.0958]
lons = [141.3545,139.6503,140.8694,145.8336]
names = ['Sapporo','Tokyo','Sendai','Kunashiri']
x, y = m(lons, lats)
m.scatter(x, y, 20, color="black", marker="o", edgecolor="k")
for i in range(len(names)):
    plt.text(x[i], y[i], names[i])

plt.savefig("locations.png",bbox_inches='tight')

 