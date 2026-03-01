import pandas as pd

# Load the CSV
df = pd.read_csv('AusApparalSales4thQrt2020.csv')

# Quick look
print(df.head())
print(df.info())

# Drop rows where all elements are NaN
df.dropna(how='all', inplace=True)
# Drop duplicate rows
df.drop_duplicates(inplace=True)
# Reset index
df.reset_index(drop=True, inplace=True)

# Strip whitespace from column names
df.columns = df.columns.str.strip()

# Convert 'Date' to datetime
df['Date'] = pd.to_datetime(df['Date'], format='%d-%b-%Y', errors='coerce')

# Ensure 'Unit' and 'Sales' are numeric
df['Unit'] = pd.to_numeric(df['Unit'], errors='coerce')
df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')


# Check for nulls
print("IS NA",df.isna().sum())

# Drop rows with missing critical values
df.dropna(subset=['Date', 'State', 'Group', 'Unit', 'Sales'], inplace=True)
# Add Day of Week
df['Day'] = df['Date'].dt.day_name()

# Add Revenue per Unit
df['Revenue_per_Unit'] = df['Sales'] / df['Unit']

print("Describe\n", df.describe())
# Save cleaned data
df.to_csv('AusApparalSales4thQrt2020_cleaned.csv', index=False)