## Task 1 - Make a plot showing the temporal evoltuion (2001-2006) of total Argo float numbers for a specific region

#Import Python modules

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd

#Import Argo float csv files for each year

df_1 = pd.read_csv('argo_1.csv', parse_dates=[15])
df_2 = pd.read_csv('argo_2.csv', parse_dates=[15])
df_3 = pd.read_csv('argo_3.csv', parse_dates=[15])
df_4 = pd.read_csv('argo_4.csv', parse_dates=[15])
df_5 = pd.read_csv('argo_5.csv', parse_dates=[15])
df_6 = pd.read_csv('argo_6.csv', parse_dates=[15])
df_7 = pd.read_csv('argo_7.csv', parse_dates=[15])
df_8 = pd.read_csv('argo_8.csv', parse_dates=[15])
df_9 = pd.read_csv('argo_9.csv', parse_dates=[15])
df_10 = pd.read_csv('argo_10.csv', parse_dates=[15])
df_11 = pd.read_csv('argo_11.csv', parse_dates=[15])
df_12 = pd.read_csv('argo_12.csv', parse_dates=[15])

#Use geopandas to import shapefiles of countries and continents to be used in the subsequent plot

countries = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))  #Read a datafile from geopandas with country b>

print(countries["continent"])


# Define subplots layout

fig, ax = plt.subplots(nrows=3, ncols=2, figsize=(15,15))

# Plot North America shapefile obtained from geopandas on each plot

countries[countries["continent"] == "Oceania"].plot(ax=ax[0,0],color="black")
countries[countries["continent"] == "Oceania"].plot(ax=ax[1,0],color="black")
countries[countries["continent"] == "Oceania"].plot(ax=ax[2,0],color="black")
countries[countries["continent"] == "Oceania"].plot(ax=ax[0,1],color="black")
countries[countries["continent"] == "Oceania"].plot(ax=ax[1,1],color="black")
countries[countries["continent"] == "Oceania"].plot(ax=ax[2,1],color="black")
countries[countries["continent"] == "Oceania"].plot(ax=ax[0,0],color="black")
countries[countries["continent"] == "Oceania"].plot(ax=ax[1,0],color="black")
countries[countries["continent"] == "Oceania"].plot(ax=ax[2,0],color="black")
countries[countries["continent"] == "Oceania"].plot(ax=ax[0,1],color="black")
countries[countries["continent"] == "Oceania"].plot(ax=ax[1,1],color="black")
countries[countries["continent"] == "Oceania"].plot(ax=ax[2,1],color="black")
# Plot total number of argo floats for each year

df_1.plot(ax=ax[0,0], x="LONGITUDE", y="LATITUDE", kind="scatter", c="red", colormap="viridis", vmin =1, vmax=12, s=1)
ax[0, 0].set_title(f'Argo Floats in June (Total # of Floats = {len(df_1)})')
df_2.plot(ax=ax[1,0], x="LONGITUDE", y="LATITUDE", kind="scatter", c="red", colormap="viridis", vmin =1, vmax =12, s=1)
ax[1, 0].set_title(f'Argo Floats in July (Total # of Floats = {len(df_2)})')
df_3.plot(ax=ax[2,0], x="LONGITUDE", y="LATITUDE", kind="scatter", c="red", colormap="viridis", vmin =1, vmax =12, s=1)
ax[2, 0].set_title(f'Argo Floats in August (Total # of Floats = {len(df_3)})')
df_4.plot(ax=ax[0,1], x="LONGITUDE", y="LATITUDE", kind="scatter", c="red", colormap="viridis", vmin =1, vmax =12, s=1)
ax[0, 1].set_title(f'Argo Floats in September (Total # of Floats = {len(df_4)})')
df_5.plot(ax=ax[1,1], x="LONGITUDE", y="LATITUDE", kind="scatter", c="red", colormap="viridis", vmin =1, vmax = 12, s=1)
ax[1, 1].set_title(f'Argo Floats in October (Total # of Floats = {len(df_5)})')
df_6.plot(ax=ax[2,1], x="LONGITUDE", y="LATITUDE", kind="scatter", c="red", colormap="viridis", vmin =1, vmax=12, s=1)
ax[2, 1].set_title(f'Argo Floats in November (Total # of Floats = {len(df_6)})')


# Add grids and plot layout
ax[0, 0].grid()
ax[1, 0].grid()
ax[2, 0].grid()
ax[0, 1].grid()
ax[1, 1].grid()
ax[2, 1].grid()


fig.tight_layout()
plt.savefig('monthly.png')

