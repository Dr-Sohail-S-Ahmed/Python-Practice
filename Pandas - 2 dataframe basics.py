import pandas as pd

df = pd.read_csv("movies-db.csv")   # no need to import csv module
print(df.head(3))   # prints 1st 'n' rows

print(df.industry.unique())     # only prints unique items (no duplicates)
print(df.language.unique())     # only prints unique items (no duplicates)

print(df.industry.value_counts())   # prints count for each unique value
print(df.language.value_counts())   # prints count for each unique value

print(df[["title","imdb_rating","industry"]])   # prints only specified columns i.e. column filtering

print(df[df.release_year>2000])     # prints only