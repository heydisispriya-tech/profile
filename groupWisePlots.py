import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("AusApparalSales4thQrt2020_Cleaned.csv")

# Drop rows with missing values (if any)
df.dropna(inplace=True)

# Group-wise sales aggregation by State
group_sales = df.groupby(['State', 'Group'])['Sales'].sum().unstack().fillna(0)

# Display the summary table
print("Group-wise Sales by State:")
print(group_sales)

# Plotting the sales distribution
plt.figure(figsize=(12, 6))
group_sales.plot(kind='bar', stacked=False, colormap='tab10')
plt.title("Group-wise Sales Across States")
plt.ylabel("Total Sales (₹)")
plt.xlabel("State")
plt.xticks(rotation=45)
plt.legend(title="Group")
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
