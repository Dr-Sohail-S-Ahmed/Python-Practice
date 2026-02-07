import pandas as pd

df = pd.read_csv("movies-db.csv")   # no need to import csv module

    # (COLUMN LEVEL FILTERING)
print(df.industry.unique())     # only prints unique items (no duplicates)
print(df.language.unique())     # only prints unique items (no duplicates)
print(df.industry.value_counts())   # prints count for each unique value
print(df.language.value_counts())   # prints count for each unique value
print(df[["title","imdb_rating","industry"]])   # prints only specified columns

    # (ROW LEVEL FILTERING)
print(df.head(3))   # prints 1st 'n' rows
print(df[df.release_year>2000])     # prints only rows based on specific criteria
print(df[df.studio=="Marvel Studios"])      # prints only rows meeting specific criteria
print(df.describe())    # for all numeric columns, prints basic stats
print(df.info())    # prints info regarding the columns
print(df[(df.imdb_rating == df.imdb_rating.max()) | (df.imdb_rating == df.imdb_rating.min())])
    # prints max & min of a specific numeric column + "|" refers to "OR"

current_year = pd.Timestamp.now().year      # to get current year dynamically
df["age"] = df["release_year"].apply(lambda x: current_year - x)
    # adding "age" column + "lambda" is a nameless, single-expression function meant for quick, disposable logic...
    # ...i.e. for row iteration, it takes the respective value for the respective row
print(df.head(4))   # now, prints additional column of age with 1st 'n' rows

df["profit"] = df.apply(lambda x: x["revenue"] - x["budget"], axis=1)   # calculating profit based on revenue & budget
    # 'axis=0' → Move down each column, pass whole column to function
    # 'axis=1' → Move across each row, pass whole row to function
print(df.head(5))   # now, prints print column also for 'n' rows

print(df.index)     # shows indexing of table i.e. start, stop & next index increase rate

df.set_index("title", inplace=True)
    # index (0,1,2,etc.) is replaced by the items of specified col + 'inplace' is to modify original data
print(df.head(3))   # prints 'n' rows with title as index instead of numbers
print(df.index)     # prints titles as indexes
print(df.loc["Race 3"])     # using title as index, details are printed
print(df.loc["Race 3"].shape)   # returns only no. of col i.e. 1D
print(df.loc[["Race 3"]].shape) # returns no. of rows & no. of cols or (row,col) i.e. 2D
print(df.loc[["Race 3", "Bajrangi Bhaijaan"]])      # Note: double square brackets for 2D otherwise error
print(df.iloc[0])   # prints integer based location (while index nos. aren't printed)
print(df.iloc[0:2]) # prints integer based location range

print(df[~df["language"].isin(["Hindi","English"])])
    # prints movies that don't match criteria + '~' means 'not' & 'isin' is like 'IN' in SQL

print("<same data as series>")
print(df.groupby("industry")["revenue"].mean())
    # 'groupby()' method doesn't compute anything but organizes data + [""] is col selection
print("<same data as dataframe>")
print(df.groupby("industry")[["revenue"]].mean())

print(df.sort_values(by="profit", ascending=False).head(5))
    # prints 'n' rows of profit in descending order + 'sort_values' method sort Series of DataFrame by values of 1 or more col

df.reset_index(inplace=True)    # reverts back to the original form
print(df.head(3))   # prints the original