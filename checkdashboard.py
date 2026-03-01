import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load and clean data
df = pd.read_csv("AusApparalSales4thQrt2020.csv")
df.dropna(inplace=True)

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Create time buckets
df['Week'] = df['Date'].dt.isocalendar().week
df['Month'] = df['Date'].dt.month
df['Quarter'] = df['Date'].dt.quarter

plt.figure(figsize=(14, 5))
sns.lineplot(data=df, x='Date', y='Sales', hue='Group')
plt.title("📅 Daily Sales Trend by Customer Group")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


plt.figure(figsize=(12, 5))
sns.boxplot(data=df, x='Week', y='Sales', hue='Group')
plt.title("📈 Weekly Sales Distribution by Group")
plt.xlabel("Week Number")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()


monthly_sales = df.groupby(['Month', 'Group'])['Sales'].sum().reset_index()

plt.figure(figsize=(10, 5))
sns.barplot(data=monthly_sales, x='Month', y='Sales', hue='Group')
plt.title("📊 Monthly Sales by Group")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()


quarterly_sales = df.groupby(['Quarter', 'Group'])['Sales'].sum().reset_index()

plt.figure(figsize=(8, 5))
sns.barplot(data=quarterly_sales, x='Quarter', y='Sales', hue='Group')
plt.title("📉 Quarterly Sales Summary")
plt.xlabel("Quarter")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()
