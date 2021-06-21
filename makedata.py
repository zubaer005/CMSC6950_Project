## Task 1 Continued - Import argopy_task1.csv and seperate Argo float data into dataframes for each year

#Import Python modules

import numpy as np
import pandas as pd

#Import Argo float csv file as a data frame and assign date column

df = pd.read_csv('task1.csv', parse_dates=[15])

#Add a year column to the dataframe

df['year'] = pd.DatetimeIndex(df['TIME']).month

#Seperate the dataframe into data frames for each year


df_jan = df[df['TIME'].dt.month == 1] ##Create a dataframe for data collected in 1
df_feb = df[df['TIME'].dt.month == 2] ##Create a dataframe for data collected in 2
df_mar = df[df['TIME'].dt.month == 3] ##Create a dataframe for data collected in 3
df_apr = df[df['TIME'].dt.month == 4] ##Create a dataframe for data collected in 4
df_may = df[df['TIME'].dt.month == 5] ##Create a dataframe for data collected in 5
df_jun = df[df['TIME'].dt.month == 6] ##Create a dataframe for data collected in 6
df_jul = df[df['TIME'].dt.month == 7] ##Create a dataframe for data collected in 7
df_aug = df[df['TIME'].dt.month == 8] ##Create a dataframe for data collected in 8
df_sep = df[df['TIME'].dt.month == 9] ##Create a dataframe for data collected in 9
df_oct = df[df['TIME'].dt.month == 10] ##Create a dataframe for data collected in 10
df_nov = df[df['TIME'].dt.month == 11] ##Create a dataframe for data collected in 11
df_dec = df[df['TIME'].dt.month == 12] ##Create a dataframe for data collected in 12

##Calcuate the total number of argo floats each year by appending dataframes

d1 = df_jan.append(df_feb) 
d2 = d1.append(df_mar) 
d3 = d2.append(df_apr) 
d4 = d3.append(df_may) 
d5 = d4.append(df_jun) 
d6 = d5.append(df_jul)
d7 = d6.append(df_aug) 
d8 = d7.append(df_sep) 
d9 = d8.append(df_oct) 
d10 = d9.append(df_nov) 
d11 = d10.append(df_dec) 
 
#Export each data frame to a csv file

df_jan.to_csv (r'argo_1.csv', index = False, header=True)
d1.to_csv (r'argo_2.csv', index = False, header=True)
d2.to_csv (r'argo_3.csv', index = False, header=True)
d3.to_csv (r'argo_4.csv', index = False, header=True)
d4.to_csv (r'argo_5.csv', index = False, header=True)
d5.to_csv (r'argo_6.csv', index = False, header=True)
d6.to_csv (r'argo_7.csv', index = False, header=True)
d7.to_csv (r'argo_8.csv', index = False, header=True)
d8.to_csv (r'argo_9.csv', index = False, header=True)
d9.to_csv (r'argo_10.csv', index = False, header=True)
d10.to_csv (r'argo_11.csv', index = False, header=True)
d11.to_csv (r'argo_12.csv', index = False, header=True)

