import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load and clean the dataset
df = pd.read_csv("AusApparalSales4thQrt2020.csv")

# Remove rows with missing or invalid 'State' and 'Sales'
df = df.dropna(subset=['State', 'Sales'])
df = df[df['State'].str.strip() != '']
df = df[df['Sales'].apply(lambda x: str(x).strip().isdigit())]

# Convert 'Sales' to numeric (in case it's read as string)
df['Sales'] = pd.to_numeric(df['Sales'])

# Define low-revenue states*
state_sales = df.groupby('State')['Sales'].sum().sort_values(ascending=False)


df['State'] = df['State'].str.strip().str.upper()
state_sales.index = state_sales.index.str.strip().str.upper()
low_revenuedf = state_sales.tail(3)
# Get the bottom 3 states with lowest sales
low_revenue_states = low_revenuedf.index.tolist()


# Filter data for low-revenue states
low_df = df[df['State'].isin(low_revenue_states)]
print("Filtered Data for Low Revenue States:")
print(low_df)
# Current total sales by state
current_sales = low_df.groupby('State')['Sales'].sum()

# Define hypothetical uplift percentages for each program
uplift = {
    'Referral Program': 0.10,
    'Geo-Promotion': 0.15,
    'Bundle Offer': 0.12,
    'CRM Re-engagement': 0.08,
    'Localized Inventory': 0.10
}

# Simulate ROI
roi_data = []

for state in low_revenue_states:
    for program, percent in uplift.items():
        current = current_sales.get(state, 0)
        expected = current * (1 + percent)
        increment = expected - current
        roi_data.append({
            'State': state,
            'Program': program,
            'Current Sales': current,
            'Expected Sales': expected,
            'Increment': increment
        })

roi_df = pd.DataFrame(roi_data)

# Display results
print(roi_df.sort_values(by='Increment', ascending=False))






# Optional: sort for better visuals
roi_df_sorted = roi_df.sort_values(by='Increment', ascending=False)

plt.figure(figsize=(12, 6))
sns.barplot(data=roi_df_sorted, x='State', y='Increment', hue='Program')
plt.title("Estimated Sales Uplift by Program in Low-Revenue States")
plt.ylabel("Incremental Sales (₹)")
plt.xlabel("State")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
