import pandas as pd
from scipy import stats

# Load the dataset
df = pd.read_csv('AusApparalSales4thQrt2020_cleaned.csv')

# Drop rows with missing values in Sales or Unit
df = df.dropna(subset=['Sales', 'Unit'])

# Mean
sales_mean = df['Sales'].mean()
unit_mean = df['Unit'].mean()

# Median
sales_median = df['Sales'].median()
unit_median = df['Unit'].median()

# Mode
sales_mode = df['Sales'].mode()[0]
unit_mode = df['Unit'].mode()[0]

# Standard Deviation
sales_std = df['Sales'].std()
unit_std = df['Unit'].std()

# Display results
print(f"Sales - Mean: {sales_mean:.2f}, Median: {sales_median}, Mode: {sales_mode}, Std Dev: {sales_std:.2f}")
print(f"Unit  - Mean: {unit_mean:.2f}, Median: {unit_median}, Mode: {unit_mode}, Std Dev: {unit_std:.2f}")
