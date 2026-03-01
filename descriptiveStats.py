import pandas as pd

# Load the dataset
df = pd.read_csv('AusApparalSales4thQrt2020.csv')

# Drop rows with missing values in 'Group' or 'Sales'
df = df.dropna(subset=['Group', 'Sales'])

# Group by demographic group and sum sales
group_sales = df.groupby('Group')['Sales'].sum().sort_values(ascending=False)

# Display results
print("Total Sales by Group:")
print(group_sales)

# Identify highest and lowest
highest_group = group_sales.idxmax()
lowest_group = group_sales.idxmin()

print(f"\n🔝 Highest Sales Group: {highest_group} with ₹{group_sales.max():,.0f}")
print(f"🔻 Lowest Sales Group: {lowest_group} with ₹{group_sales.min():,.0f}")
