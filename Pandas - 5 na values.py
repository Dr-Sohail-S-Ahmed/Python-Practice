from hmac import new

import pandas as pd
import numpy as np

df = pd.read_csv('weather_data_na.csv')


print('<---ORIGINAL--->')
print(df)

print('<---REPLACING VALUES--->')
df.replace([-99999,-88888], np.nan, inplace=True)
    # 'np.nan' can be changed to '0'
    # '[]' is used when list is to-be-replaced
    # 'df.replace([-99999,-88888], np.nan, inplace=True)' is the same as
        # ...'df.replace(to_replace=[-99999,-88888], value=np.nan, inplace=True)'
    #
print(df)

print('<---REPLACING MULTIPLE VALUES (COLUMN-WISE)--->')
df = pd.read_csv('weather_data_na.csv')
df.replace({
    'temperature': -99999,
    'windspeed': [-99999,-88888],
    'event': 'no event',
}, np.nan, inplace=True)
print(df)

print('<---REPLACING MULTIPLE VALUES (GENERAL)--->')
df = pd.read_csv('weather_data_na.csv')
df.replace({
    -99999: np.nan,
    -88888: np.nan,
    'no event': 'Sunny'
}, inplace=True)
print(df)

new_df = pd.DataFrame({
    'score': ['exceptional', 'average', 'good', 'poor', 'average', 'exceptional'],
    'names': ['Tom', 'Dick', 'Harry', 'Charsi', 'Champu', 'Chutia']
})
print(new_df)
new_df.replace(['exceptional', 'good', 'average', 'poor'],[4, 3, 2, 1], inplace=True)
print(new_df)