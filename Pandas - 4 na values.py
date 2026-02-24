import pandas as pd

print('<---ORIGINAL--->')
df = pd.read_csv('weather_data.csv')
print(df)
print(type(df.day[0]))      # verifying data type for a value i.e. day → string
print(df['day'].dtype)      # verifying data type for the entire series/column

print('<---CONVERTED TO TIMESTAMP--->')
df = pd.read_csv('weather_data.csv', parse_dates=['day'])   # converts specified columns into datetime objects when reading data
print(df)
print(type(df.day[0]))      # converted to 'Timestamp' (for single value) i.e. day → datetime64[ns]
print(df['day'].dtype)      # converted to 'datatime64[ns]' (for entire column) (for single value) i.e. day → datetime64[ns]

print('<---TURNING COLUMN INTO INDEX--->')
df.set_index('day', inplace=True)
print(df)

print("<---REPLACING N/A VALUES--->")
df.fillna(0, inplace=True)      # replaces n/a values with '0'
print(df)

df0 = pd.read_csv('weather_data.csv')
df0.fillna({
    'temperature': df.temperature.mean(),
    'windspeed': df.windspeed.mean(),
    'event': 'No Event'
})      # replaces n/a value with custom values for each column
print(df0)