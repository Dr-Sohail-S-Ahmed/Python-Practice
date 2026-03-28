import pandas as pd

df = pd.read_csv('weather_by_cities.csv')
print(df)

print('<---DATA BY CITY--->')
print(df[df.city=='new york'])

print('<---TEMPERATURE BY CITY--->')
print(df[df.city=='new york'].temperature.max())

print('<---GROUP BY CITY--->')
g = df.groupby('city')
print(g)    # Data type
for city, data in g:
    print('\n')
    print(city)
    print('data:', data)
    print('max temp:', data.temperature.max())
    print('min temp:', data.temperature.min())

print('<---GET GROUP--->')
print(g.get_group('paris'))
print(g.max())
    # Gives maximum of each column value while for string alphabetically largest
print(g.min())
print(df.groupby('city')[['temperature','windspeed']].mean())
    # 'print(g.mean())' gives error bcz of non-numeric column
    # 'print(g[['temperature','windspeed']].mean())' also gives the same result
print(g.describe())
    # Gives stats
print(g.size())
    # Gives size of DataFrame alongwith data type

import time
print('<---CUSTOM GROUPING 1--->')
start = time.perf_counter()
def grouper (df, idx, col):
    if 80 <= df[col].loc[idx] <= 90:
        return '80-90'
    elif 50 <= df[col].loc[idx] <= 60:
        return '50-60'
    else:
        return 'others'

g = df.groupby(lambda idx: grouper(df, idx, 'temperature'))
print(g)

for key, data in g:
    print('Key:', key)
    print('Data:', data)
end = time.perf_counter()
print(f'Total time: {end-start}')

print('<---CUSTOM GROUPING 2--->')
    # This one is CLEANER & MORE EFFICIENT
start = time.perf_counter()
df['temp_group'] = df['temperature'].apply(
    lambda x: '80-90' if 80 <= x <= 90
    else '50-60' if 50 <= x <= 60
    else 'others'
)
    # '.apply()' applies a function to each value in a column

g = df.groupby('temp_group')
print(g)

for k, d in g:
    print('Key:', k)
    print('Data:', d)
end = time.perf_counter()
print(f'Total time: {end-start}')

# Time difference doesn't prove code efficiency but rather 2nd code accesses data directly