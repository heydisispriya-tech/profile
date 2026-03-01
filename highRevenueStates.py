import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("AusApparalSales4thQrt2020.csv")

# Drop rows with missing values in 'State' or 'Sales'
df = df.dropna(subset=['State', 'Sales'])

# Group by State and sum the Sales
state_sales = df.groupby('State')['Sales'].sum().sort_values(ascending=False)
print("top 3 states with highest sales:")
print(state_sales)
  
