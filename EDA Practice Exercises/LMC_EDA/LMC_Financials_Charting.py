import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dfa = pd.read_csv("annual_report.csv",
                  skiprows=1,
                  skipfooter=1,
                  engine='python')
dfe = pd.read_csv("expenditures.csv",
                  skiprows=1,
                  skipfooter=1,
                  engine='python')
dfp = pd.read_csv("purchase.csv",
                  skiprows=1)
dfr = pd.read_csv("revenue.csv",
                  skiprows=[0,1,2],
                  skipfooter=2,
                  engine='python')
dfr.columns = ['date',
               'Jul-25_100','Jul-25_50',
               'Aug-25_100','Aug-25_50',
               'Sep-25_100','Sep-25_50',
               'Oct-25_100','Oct-25_50',
               'Nov-25_100','Nov-25_50',
               'Dec-25_100','Dec-25_50',
               'Jan-26_100','Jan-26_50',
               'Feb-26_100','Feb-26_50',
               'Mar-26_100','Mar-26_50']


# 'skipfooter' not supported in C engine therefore selected Python engine

print(dfr.head())

# Filter diesel only
diesel = dfp[dfp['Item Name'] == 'Diesel']

plt.plot(diesel['Date'], diesel['Total Payment'], 'o-')
plt.xlabel('Date')
plt.ylabel('Total Payment')
plt.title('Diesel Purchase Amount Over Time')
plt.xticks(rotation=45)
plt.show()



plt.figure(figsize=(12,5))
plt.plot(dfa['Month-Year'], dfa['Net Income'], 'o-', linewidth=2)
plt.fill_between(dfa['Month-Year'], dfa['Net Income'], alpha=0.3)
plt.xticks(rotation=45,size=7)
plt.title('Net Income Trend')
plt.grid(True, alpha=0.3)
plt.show()



# Create restructured data
data = {
    'Month': ['Jul25', 'Aug25', 'Sep25', 'Oct25', 'Nov25', 'Dec25', 'Jan26', 'Feb26', 'Mar26'],
    'Diesel': [65040, 46571, 67785, 69150, 71400, 53362, 0, 53900, 47198],
    'Medical': [0, 0, 0, 0, 0, 0, 79450, 0, 0]
}

dfe = pd.DataFrame(data)
dfe.plot(x='Month', kind='bar', stacked=True, figsize=(12,6))
plt.title('Monthly Expenditure by Category')
plt.ylabel('Amount')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(12,5))
plt.plot(dfe['Month'], dfe['Diesel'], 'o-', linewidth=2, markersize=8, color='black')
plt.fill_between(dfe['Month'], dfe['Diesel'], alpha=0.2, color='gray')
plt.title('Monthly Diesel Expenditure Trend')
plt.ylabel('Amount')
plt.xticks(rotation=45)
for i, v in enumerate(dfe['Diesel']):
    plt.text(i, v + 2000, f'{v:,.0f}', ha='center')
plt.grid(True, alpha=0.3)
plt.show()


sizes = [527906, 79450]
labels = ['Diesel', 'Medical']
colors = ['#ff9999', '#66b3ff']
explode = (0.05, 0)

plt.figure(figsize=(8,8))
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)
plt.title('Total Expenditure by Category (9 Months)')
plt.show()



# Data preparation
months = ['Jul25', 'Aug25', 'Sep25', 'Oct25', 'Nov25', 'Dec25', 'Jan26', 'Feb26', 'Mar26']
revenue_100 = [131180, 109280, 122830, 139860, 145260, 137810, 140890, 126910, 99380]
revenue_50 = [66129, 55729, 70573, 72718, 76198, 73703, 90786, 74791, 70581]
carry = [539, 1089, 9158, 2788, 3568, 4798, 20341, 11336, 20891]

# Create DataFrame
dfr = pd.DataFrame({
    'Month': months,
    'Revenue_100': revenue_100,
    'Revenue_50': revenue_50,
    'Carry': carry,
    'Ratio': [r100/r50 for r100, r50 in zip(revenue_100, revenue_50)]
})

# 1. Grouped Bar Chart
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

x = np.arange(len(months))
width = 0.35

ax1.bar(x - width/2, revenue_100, width, label='100% Charge', color='darkgreen')
ax1.bar(x + width/2, revenue_50, width, label='50% Charge', color='lightgreen')
ax1.set_xlabel('Month')
ax1.set_ylabel('Revenue')
ax1.set_title('Monthly Revenue Comparison')
ax1.set_xticks(x)
ax1.set_xticklabels(months, rotation=45)
ax1.legend()
ax1.grid(True, alpha=0.3)

# 2. Carry Trend
ax2.plot(months, carry, 'o-', linewidth=2, markersize=8, color='orange')
ax2.fill_between(months, carry, alpha=0.3, color='orange')
ax2.set_xlabel('Month')
ax2.set_ylabel('Carry Amount')
ax2.set_title('Monthly Carry-Forward Trend')
ax2.tick_params(axis='x', rotation=45)
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# 3. Ratio Analysis
plt.figure(figsize=(12,5))
plt.plot(months, dfr['Ratio'], 'o-', linewidth=2, markersize=8, color='purple')
plt.axhline(y=2.0, color='red', linestyle='--', label='Theoretical Max (2.0)')
plt.axhline(y=dfr['Ratio'].mean(), color='blue', linestyle='--',
            label=f"Average: {dfr['Ratio'].mean():.2f}")
plt.title('100% vs 50% Revenue Ratio Over Time')
plt.xlabel('Month')
plt.ylabel('Ratio')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# 4. Summary Statistics
print("=" * 50)
print("REVENUE SUMMARY STATISTICS")
print("=" * 50)
print(f"\nTotal Revenue (100%): {sum(revenue_100):,.0f}")
print(f"Total Revenue (50%):   {sum(revenue_50):,.0f}")
print(f"Total Carry Forward:   {sum(carry):,.0f}")
print(f"\nAverage Monthly Revenue:")
print(f"  100% Charge: {np.mean(revenue_100):,.0f}")
print(f"  50% Charge:  {np.mean(revenue_50):,.0f}")
print(f"\nBest Month (100%): {months[np.argmax(revenue_100)]} with {max(revenue_100):,.0f}")
print(f"Worst Month (100%): {months[np.argmin(revenue_100)]} with {min(revenue_100):,.0f}")