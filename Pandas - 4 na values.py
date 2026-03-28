import pandas as pd

print('<---ORIGINAL--->')
df = pd.read_csv('weather_data.csv')
print(df)
print(type(df.day[0]))      # verifying data type for a value i.e. day → string
print(df['day'].dtype)      # verifying data type for the entire series/column

print('<---CONVERTED TO PROPER TIMESTAMP (FOR DAY COLUMN)--->')
df = pd.read_csv('weather_data.csv', parse_dates=['day'])   # converts specified columns into datetime objects when reading data
print(df)
print(type(df.day[0]))      # converted to 'Timestamp' (for single value) i.e. day → datetime64[ns]
print(df['day'].dtype)      # converted to 'datatime64[ns]' (for entire column) (for single value) i.e. day → datetime64[ns]

print('<---TURNING COLUMN INTO INDEX--->')
df.set_index('day', inplace=True)
print(df)
print(df.dtypes)        # Gives data types for all columns

print('<---REPLACING N/A VALUES--->')
    # "df.fillna(0, inplace=True)" would replace n/a (aka NaN) values with '0' in older versions of Pandas but...
    # ...in the newer version if any column has string datatype, this'll give an error

print('...original values...')
df = pd.read_csv('weather_data.csv')
print(df)
print('...custom values...')
df.fillna({
    'temperature': df.temperature.mean(),
    'windspeed': df.windspeed.mean(),
    'event': 'No Event',
}, inplace=True)      # replaces n/a value with custom values for each column
print(df)

print('...original values...')
df = pd.read_csv('weather_data.csv')
print(df)
print('...forward-filled values vertically...')
df = pd.read_csv('weather_data.csv')
df.ffill(inplace=True)
# df.fillna(method='ffill')
print(df)
    # Older versions of Pandas accepted "df.fillna(method='ffill')"

print('...original values...')
df = pd.read_csv('weather_data.csv')
print(df)
print('...backward-filled values vertically...')
df.bfill(inplace=True)
print(df)
    # Older versions of Pandas accepted "df.fillna(method='bfill')"

print('...original values...')
df = pd.read_csv('weather_data.csv')
print(df)
print('...forward-filled values horizontally...')
df = df.ffill(axis=1)       # 'axis=0' or 'axis='rows' for rows, 'axis=1' or axis='columns' for columns
    # 'df = df.ffill(axis=1, limit=1)' limits forward-fill to 'n' place
    # Use 'df.ffill(axis=1, inplace=True)', if want to modify the same DataFrame but Pandas v2.x+ don't support 'inplace'
print(df)

print('...original values...')
df = pd.read_csv('weather_data.csv')
print(df)
print('...backward-filled values horizontally...')
df = df.bfill(axis=1)       # 'axis=0' or 'axis='rows' for rows, 'axis=1' or axis='columns' for columns
    # 'df = df.bfill(axis=1, limit=1)' limits backward-fill to 'n' place
    # Use 'df.bfill(axis=1, inplace=True)', if want to modify the same DataFrame but Pandas v2.x+ don't support 'inplace'
print(df)

print('...original values...')
df = pd.read_csv('weather_data.csv')
print(df)
print('...interpolate values (insert middle value in missing ones)...')
df[['temperature','windspeed']] = df[['temperature','windspeed']].interpolate()
    # Syntax 'df = df.interpolate()' works when all data is numeric
print(df)

print('...interpolate values based on time...')

    # converts specified columns into datetime objects when reading data
df = pd.read_csv('weather_data.csv', parse_dates=['day'])

    # converts date to index [required for time-based interpolation]
df.set_index('day', inplace=True)
print(df)

    # Ensure daily frequency by adding missing dates
df = df.asfreq('D')     # 'D' is frequency alias + others include 'B' (business day), 'W' (weekly),...
                        # ...'M' (month end), 'MS' (month start), 'H' (hourly), 'T' or 'min' (minute)

    # Interpolate numeric columns only by adding middle value between values above & below it
numeric_cols = ['temperature', 'windspeed']
df[numeric_cols] = df[numeric_cols].interpolate(method='time')
print(df)

print('<---TRANSPOSING DATA--->')
df = df.T   # Or 'df.transpose()' to transpose data
print(df)