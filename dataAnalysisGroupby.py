import pandas as pd
import numpy as np  
df = pd.read_csv('AusApparalSales4thQrt2020.csv')

grouped = df.groupby('State')
for state, chunk in grouped:
    print(f"{state} has {len(chunk)} records")

state_sales = df.groupby('State')['Sales'].sum().reset_index()
df_merged = df.merge(state_sales, on='State', suffixes=('', '_Total'))
print(df_merged.head(10))
df_grouped = df.groupby(['State', 'Group']).agg({'Unit': 'sum', 'Sales': 'sum'}).reset_index()
print(df_grouped.head(10))
df_grouped['Sales_Per_Unit'] = df_grouped['Sales'] / df_grouped['Unit']
print(df_grouped.head(10))    
# Save grouped data
df_grouped.to_csv('AusApparalSales4thQrt2020_grouped.csv', index=False)
# Save merged data
df_merged.to_csv('AusApparalSales4thQrt2020_merged.csv', index=False)
