from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler

import pandas as pd
import numpy as np

# Select columns to normalize
num_cols = ['Unit', 'Sales', 'Revenue_per_Unit']


# Initialize scaler
minmax = MinMaxScaler()
df = pd.read_csv('AusApparalSales4thQrt2020_cleaned.csv')
# Apply scaling
df_minmax = df.copy()
df_minmax[num_cols] = minmax.fit_transform(df[num_cols])

print(df_minmax[num_cols].head())

# Initialize scaler
standard = StandardScaler()

# Apply scaling
df_standard = df.copy()
df_standard[num_cols] = standard.fit_transform(df[num_cols])

print(df_standard[num_cols].head())
