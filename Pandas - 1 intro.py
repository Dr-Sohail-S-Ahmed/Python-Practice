# PANDAS = Panel Data

# THE FOLLOWING IS HOW DATA IS ANALYZED IN PYTHON
import csv

with open("movies-db.csv") as f:
    data = list(csv.reader(f))
    header = data[0]
    data = data[1:]
    # Any called row that's empty in the csv file would result in error while running this code

    # (DATA ANALYSIS CODE)
def calculate_rating_stats (data, industry=None):
    ratings = []
    for row in data:
        if row[3]!="NULL" and (not industry or row[1]==industry):   # Keep rows that have a rating and,
                                                                    # if an industry is given, match that industry
                                                                    # (where col 3 has rating, col 1 has industry)
            ratings.append(float(row[3]))
    max_rating = max(ratings)
    min_rating = min(ratings)
    avg_rating = sum(ratings) / len(ratings)
    return max_rating, min_rating, avg_rating

max_rating, min_rating, avg_rating = calculate_rating_stats(data)
print(f"All records: Min rating = {min_rating}, Max rating = {max_rating}, Avg rating = {avg_rating}")

max_rating, min_rating, avg_rating = calculate_rating_stats(data, industry="Bollywood")
print(f"Bollywood records: Min rating = {min_rating}, Max rating = {max_rating}, Avg rating = {avg_rating}")

max_rating, min_rating, avg_rating = calculate_rating_stats(data, industry="Hollywood")
print(f"Hollywood records: Min rating = {min_rating}, Max rating = {max_rating}, Avg rating = {avg_rating}")


# THE FOLLOWING IS HOW DATA IS ANALYZED IN PANDAS (i.e. fewer lines of code)
import pandas as pd

df = pd.read_csv("movies-db.csv")   # Dataframe (df) is 2D labeled data structure like SQL or Excel table with rows & columns
                                    # Data can be int, float, str
    # (PRINTING)
print(df)   # Prints entire data in tabular format
print(df.head())    # Prints 1st 5 rows only
print(df.head(2))   # Prints 1st 2 rows only
print(df.tail())    # Prints last 5 rows only
print(df.tail(3))   # Prints last 3 rows only
print(df.sample(4)) # Prints random rows sample
print(df[3:8])      # Prints specified range rows only
print(df.shape)     # Prints rows & columns of the data

print(df["imdb_rating"])    # Prints entire column
print(df.imdb_rating)       # Gives the same result
print(type(df["imdb_rating"]))
print(type(df.imdb_rating))
print(type(df))
    # Column in dataframe is called "Series" + "df" is dataframe while "df.imdb_rating" is series

    # (DATA ANALYSIS CODE)
print(dir(df.imdb_rating))  # Prints list of all properties & functions
print(df.imdb_rating.min(), df.imdb_rating.max(), df.imdb_rating.mean())    # Print minimum, maximum & average ratings

df_b = df[df.industry=="Bollywood"]
df_h = df[df.industry=="Hollywood"]
    # These return new dataframes
print(f"Bolly: Min: {df_b.imdb_rating.min()}, Max: {df_b.imdb_rating.max()}, Avg: {df_b.imdb_rating.mean()}")
    # Prints min, max & avg of Bollywood movies
print(f"Holly: Min: {df_h.imdb_rating.min()}, Max: {df_h.imdb_rating.max()}, Avg: {df_h.imdb_rating.mean()}")
    # Prints min, max & avg of Hollywood movies
