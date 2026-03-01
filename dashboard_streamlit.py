import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st


# Set up Streamlit app
# Uncomment the next line to run this script with Streamlit
# Make sure to run it in the terminal with the command:
#python -m streamlit run "c:/Users/heydi/OneDrive/DataScience Course EndProject/dashboard.py"

# Load and clean data
df = pd.read_csv("AusApparalSales4thQrt2020.csv")
df.dropna(inplace=True)
df['Date'] = pd.to_datetime(df['Date'])
df['Week'] = df['Date'].dt.isocalendar().week
df['Month'] = df['Date'].dt.month
df['Quarter'] = df['Date'].dt.quarter

monthly_sales = df.groupby(['Month', 'Group'])['Sales'].sum().reset_index()
quarterly_sales = df.groupby(['Quarter', 'Group'])['Sales'].sum().reset_index()

# Streamlit layout
st.set_page_config(layout="wide")
st.title("📊 Apparel Sales Dashboard")
st.markdown("Scroll down to view daily, weekly, monthly, and quarterly insights.")

# 📅 Daily Sales Trend
st.subheader("📅 Daily Sales Trend by Group")
fig1, ax1 = plt.subplots(figsize=(14, 5))
sns.lineplot(data=df, x='Date', y='Sales', hue='Group', ax=ax1)
ax1.set_xlabel("Date")
ax1.set_ylabel("Sales")
ax1.tick_params(axis='x', rotation=45)
st.pyplot(fig1)

# 📈 Weekly Sales Pattern
st.subheader("📈 Weekly Sales Distribution by Group")
fig2, ax2 = plt.subplots(figsize=(12, 5))
sns.boxplot(data=df, x='Week', y='Sales', hue='Group', ax=ax2)
st.pyplot(fig2)

# 📊 Monthly Performance
st.subheader("📊 Monthly Sales by Group")
fig3, ax3 = plt.subplots(figsize=(10, 5))
sns.barplot(data=monthly_sales, x='Month', y='Sales', hue='Group', ax=ax3)
st.pyplot(fig3)

# 📉 Quarterly Summary
st.subheader("📉 Quarterly Sales Summary")
fig4, ax4 = plt.subplots(figsize=(8, 5))
sns.barplot(data=quarterly_sales, x='Quarter', y='Sales', hue='Group', ax=ax4)
st.pyplot(fig4)
