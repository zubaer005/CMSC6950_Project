## Task 1 - Make a plot showing the temporal evoltuion (2001-2006) of total Argo float numbers for a specific region

#Import Python modules

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd

#Import Argo float csv files for each year

df_2001 = pd.read_csv('total_argo_2001.csv', parse_dates=[15])
df_2002 = pd.read_csv('total_argo_2002.csv', parse_dates=[15])
df_2003 = pd.read_csv('total_argo_2003.csv', parse_dates=[15])
df_2004 = pd.read_csv('total_argo_2004.csv', parse_dates=[15])
df_2005 = pd.read_csv('total_argo_2005.csv', parse_dates=[15])
df_2006 = pd.read_csv('total_argo_2006.csv', parse_dates=[15])

#Use geopandas to import shapefiles of countries and continents to be used in the subsequent plot

countries = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))  #Read a datafile from geopandas with country b>




# Define subplots layout

fig, ax = plt.subplots(nrows=3, ncols=2, figsize=(15,15))

# Plot North America shapefile obtained from geopandas on each plot

countries[countries["continent"] == "North America"].plot(ax=ax[0,0],color="black")
countries[countries["continent"] == "North America"].plot(ax=ax[1,0],color="black")
countries[countries["continent"] == "North America"].plot(ax=ax[2,0],color="black")
countries[countries["continent"] == "North America"].plot(ax=ax[0,1],color="black")
countries[countries["continent"] == "North America"].plot(ax=ax[1,1],color="black")
countries[countries["continent"] == "North America"].plot(ax=ax[2,1],color="black")

# Plot total number of argo floats for each year

df_2001.plot(ax=ax[0,0], x="LONGITUDE", y="LATITUDE", kind="scatter", c="year", colormap="viridis", vmin =2001, vmax=2006, s=1)
ax[0, 0].set_title(f'Argo Floats in 2001 (Total # of Floats = {len(df_2001)})')
df_2002.plot(ax=ax[1,0], x="LONGITUDE", y="LATITUDE", kind="scatter", c="year", colormap="viridis", vmin =2001, vmax =2006, s=1)
ax[1, 0].set_title(f'Argo Floats in 2002 (Total # of Floats = {len(df_2002)})')
df_2003.plot(ax=ax[2,0], x="LONGITUDE", y="LATITUDE", kind="scatter", c="year", colormap="viridis", vmin =2001, vmax =2006, s=1)
ax[2, 0].set_title(f'Argo Floats in 2003 (Total # of Floats = {len(df_2003)})')
df_2004.plot(ax=ax[0,1], x="LONGITUDE", y="LATITUDE", kind="scatter", c="year", colormap="viridis", vmin =2001, vmax =2006, s=1)
ax[0, 1].set_title(f'Argo Floats in 2004 (Total # of Floats = {len(df_2004)})')
df_2005.plot(ax=ax[1,1], x="LONGITUDE", y="LATITUDE", kind="scatter", c="year", colormap="viridis", vmin =2001, vmax = 2006, s=1)
ax[1, 1].set_title(f'Argo Floats in 2005 (Total # of Floats = {len(df_2005)})')
df_2006.plot(ax=ax[2,1], x="LONGITUDE", y="LATITUDE", kind="scatter", c="year", colormap="viridis", vmin =2001, vmax=2006, s=1)
ax[2, 1].set_title(f'Argo Floats in 2006 (Total # of Floats = {len(df_2006)})')


# Add grids and plot layout
ax[0, 0].grid()
ax[1, 0].grid()
ax[2, 0].grid()
ax[0, 1].grid()
ax[1, 1].grid()
ax[2, 1].grid()


fig.tight_layout()
plt.savefig('total_argo.png')

