import pandas as pd

print("<---unskipped--->")
df = pd.read_csv("stock_data.csv")
print(df)   # prints even the unnecessary row & empty rows

print("<---skipped 1--->")
df = pd.read_csv("stock_data.csv", skiprows=1)  # skips 1st unwanted row
print(df)

print("<---skipped 2--->")
df = pd.read_csv("stock_data.csv", header=1)    # takes mentioned row as header & skips it
print(df)

print("<---custom header names--->")
df = pd.read_csv("stock_data.csv", header=1, names=["stock","eps","revenue","price","owner"])
    # mentioning less names than cols -> improve name alignment, mentioning more than cols -> error
print(df)

print("<---specific rows--->")
df = pd.read_csv("stock_data.csv", header=1, nrows=2)   # only 'n' rows displayed (excluding header)
print(df)

print("<---N/A value conversion 1--->")
df = pd.read_csv("stock_data.csv", header=1, na_values=
    {"eps":["not available","n.a.",-1],
    "revenue":["not available","n.a.",-1],
    "price":["not available","n.a.",-1],
    "people":["not available","n.a.",-1]})
    # converted a bunch of unneeded values & strings to proper NaN values
print(df)

print("<---N/A value conversion 2--->")
df = pd.read_csv("stock_data.csv", header=1, na_values=["not available","n.a.",-1])
print(df)

print("<---creating csv file with data analysis columns added--->")
df["pe"] = df["price"] / df["eps"]
print(df)
df.to_csv("pe.csv", index=False, header=False)      # just remove 'index' & 'header' to bring them back to file

print("<---reading excel file--->")
df_movies = pd.read_excel("movies-db.xlsx", "movies")
print(df_movies.head(4))    # prints 'n' rows of excel file sheet

df_fin = pd.read_excel("movies-db.xlsx", "financials")
print(df_fin.head(5))   # prints 'n' rows of excel file sheet

print("<---data cleaning--->")
def standardize_currency(cur):
    if cur == "$$" or cur == "dollars":
        return "USD"
    return cur

df_fin = pd.read_excel("movies-db.xlsx", "financials", converters= {"currency":standardize_currency})
print(df_fin.tail(6))
    # function 'standardize_currency' is called without () bcz 'func()' or 'standardize_currency()' means function...
    # is being run at once which'd give an error as no data is given while 'func' or 'standardize_currency' is only...
    # ...a reference telling Pandas to run it when needed in the dataset

print("<---merge data tables/sheet based on common criteria & export to file--->")
df_merged = pd.merge(df_movies, df_fin, on='movie_id')      # Equivalemt to SQL JOIN
print(df_merged)
df_merged.to_excel(
    'movies_merged.xlsx',
    sheet_name='merged',
    index=False)     # 'True' = serial nos. col, 'False' = No serial nos. col

print("<---merging data frames & exporting to 1 file--->")
df_stocks = pd.DataFrame({
    'tickers': ['OGDCL','HBL','LUCKY','KFC','FFC'],
    'prices': [526,356,522,152,215],
    'eps': [45.2,14.52,52,5.2,9.25]})
df_stocks['pe'] = df_stocks['prices'] / df_stocks['eps']
print(df_stocks)
df_weather = pd.DataFrame({
    'day': ['1/2/2026', '2/2/2026', '3/2/2026'],
    'temperature': [32,35,28],
    'event': ['Rain', 'Sunny', 'Snow']})
print(df_weather)
with pd.ExcelWriter('we_st.xlsx') as writer:
    df_weather.to_excel(writer, sheet_name='weather', index=False)
    df_stocks.to_excel(writer, sheet_name='stocks', index=True)
        # Use '.ExcelWriter' whenever multiple DataFrames must coexist in one Excel file; '.merge' changes the data, and...
        # ...'.to_excel' alone overwrites the file