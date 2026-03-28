import pandas as pd
from matplotlib import pyplot as plt    # Alternatively: 'import matplotlib.pyplot as plt'

df_sales = pd.read_excel("linechart.xlsx")
print(df_sales.head())

print('<---PLOTTING LINE CHART--->')
plt.figure(figsize=(20,12))     # 1st no. X-axis, 2nd no. Y-axis
print(plt.plot(df_sales["Quarter"], df_sales["Fridge"]))
print(plt.plot(df_sales["Quarter"], df_sales ["Dishwasher"]))
print(plt.plot(df_sales["Quarter"], df_sales ["Washing Machine"]))
plt.plot(df_sales["Quarter"], df_sales["Fridge"], color="red", label="Fridge")
plt.plot(df_sales["Quarter"], df_sales ["Dishwasher"], color="blue", label="Dishwasher")
plt.plot(df_sales["Quarter"], df_sales ["Washing Machine"], color="green", label="Washing Machine")
plt.title("Product Sales")
plt.xlabel("Revenue (million USD)")
plt.ylabel("Financial Quarters")
plt.legend()    # show labels for each line in a box
plt.show()
    # 'print()' doesn't create chart but 'plt.show()' does
    # Correct sequence: create figure → plot line → display figure


print('<---PLOTTING PIE CHART--->')
print('...summing & indexing...')
total_sales = df_sales[['Fridge', 'Dishwasher', 'Washing Machine']].sum()
print(total_sales)
print(total_sales.index)
print('...plotting...')
plt.pie(total_sales, labels=total_sales.index,
        autopct='%1.2f%%', explode=(0.1,0,0), shadow=True, startangle=140)
plt.show()
    # Custom labels: 'labels="a","b","c"'
    # In '%1.2f%%, 1st % → format specifier start, 1st no. (before decimal) → length of number,...
    # ...2nd no. (after decimal) → decimal places to show, 'f' → float, 2nd % → percentage symbol, 3rd % → format specifier end
    # 'explode=' separates part of pie from the rest & each no. specifies distance from the rest for each index
    # 'shadow=' gives 3D appearance to the chart
    # 'startangle=' turns the pie at the specified angle
plt.show()


print('<---PLOTTING BAR CHART--->')
print('...method 1...')
df_sales.plot(kind='bar', x='Quarter')
plt.xticks(rotation=45)
plt.show()
        # 'kind=' is keyword argument in Pandas DataFrame.plot() method
        # No need to specify Y-col names when all are numeric
        # '.xticks' enables rotation of X-axis labels

print('...method 2...')
df_sales_2 = df_sales.set_index('Quarter')
print(df_sales_2)
print(df_sales_2.index)
print(df_sales_2.loc['Q1 2022'])
        # 'Quarter' col set as index so it can be accessed as such therefore no need to specify X-axis for plotting also
df_sales_2.plot(kind='bar')
plt.xticks(rotation=90)
plt.show()


print('<---PLOTTING HISTOGRAM--->')
print('...histogram thru matplotlib...')
df_score = pd.read_excel("histograms.xlsx")
print(df_score.head())
plt.hist(df_score['Exam_Score'])
plt.show()
        # Not specifying the col (like df_score['Exam_Score']) would cause plotting of all the tabs data on a single histogram

print('...histogram thru seaborn (better visualization)...')
import seaborn as sb
sb.histplot(df_score['Exam_Score'], kde=True)
        # Another way: "sb.histplot(data=df_score, x='Exam_Score', kde=True)"
plt.xlabel('Score')
plt.ylabel('Count')
plt.title('Exam Scores')
plt.show()
        # Kernel Density Estimate (kde) overlay a smooth curve on top of the histogram
        # Labels appear automatically when using Seaborn but custom labels can also be added
        # Using Matplotlib & Seaborn in combination is common


print('<---PLOTTING SCATTER PLOT--->')
df_sp = pd.read_excel("scatter_plot.xlsx")
print(df_sp.head())
sb.scatterplot(data=df_sp, x='area_square_ft', y='price')
plt.show()