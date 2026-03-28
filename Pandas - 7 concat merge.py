import pandas as pd

print('<---NEW DATAFRAMES--->')
pak_weather = pd.DataFrame({
    'city': ['Karachi','Lahore','Peshawar','Islamabad'],
    'temperature': [32,40,35,16],
    'humidity': [100,85,90,70]
})
us_weather = pd.DataFrame({
    'city': ['New York','Chicago','Orlando','New Haven'],
    'temperature': [32,40,35,16],
    'humidity': [100,85,90,87]
})
print(pak_weather)
print(us_weather)


print('<---CONCATENATING DATAFRAMES--->')
df = pd.concat([pak_weather, us_weather])
print(df)

print('...ignoring dataframe index...')
df = pd.concat([pak_weather, us_weather], ignore_index=True)
print(df)

print('...creating key index...')
df = pd.concat([pak_weather, us_weather], keys=['Pakistan','USA'])
print(df)

print('...locating key...')
print(df.loc['USA'])

print('...concatenation of different dataframes...')
temperature_df = pd.DataFrame({
    'city': ['Karachi','Lahore','Peshawar','Islamabad'],
    'temperature': [32,40,35,16],
    'humidity': [26,55,70,33]
}, index=[1,2,3,4])
windspeed_df = pd.DataFrame({
    'city': ['Lahore','Karachi','Peshawar','Islamabad'],
    'windspeed': [21,50,15,26],
    'humidity': [55,26,70,33]
}, index=[2,1,3,4])
    # 'index=' defines the location index for each value which in this case is placement of city name at a particular index
df = pd.concat([temperature_df, windspeed_df], axis=1)
    # 'axis=0' operate downwards in row direction, 'axis=1' operate sideways in column direction
print(df)


print('<---MERGING DATAFRAMES--->')
df_merged = pd.merge(temperature_df,windspeed_df, on='city')
    # 'on=' uses the criteria to merge the dataframes together
print(df_merged)

print('...new dataframes...')
df1 = pd.DataFrame({
    "city": ["new york", "chicago", "orlando", "baltimore"],
    "temperature": [21,14,35,38],
})
df2 = pd.DataFrame({
    "city": ["chicago", "new york", "san diego"],
    "humidity": [65,68,71],
})
    # Table mentioned 1st is considered left while the 2nd one is right
print(df1)
print(df2)

print('...inner join (as in SQL)...')
    # Displays only common items'
dfi = pd.merge(df1, df2, on='city', how='inner')
    # Alternate syntax: "dfi = pd.merge(df1, df2, on='city')"
print(dfi)

print('...left join (as in SQL)...')
dfl = pd.merge(df1, df2, on='city', how='left')
print(dfl)

print('...right join (as in SQL)...')
dfr = pd.merge(df1, df2, on='city', how='right')
print(dfr)

print('...outer (full) join (as in SQL)...')
dfo = pd.merge(df1, df2, on='city', how='outer')
print(dfo)

print('...cross join in SQL...')
dfc = pd.merge(df1, df2, how='cross')
    # Can't be written with 'on=' bcz cross join ignores join keys entirely
print(dfc)

print('...left anti join in SQL...')
dfla = pd.merge(df1, df2, on='city', how='left_anti')
print(dfla)

print('...right anti join in SQL...')
dfra = pd.merge(df1, df2, on='city', how='right_anti')
print(dfra)