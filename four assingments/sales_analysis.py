# sales_analysis.py
# Program to analyze sales data using pandas

import pandas as pd

# Load CSV file
df = pd.read_csv("sales_data.csv")

# Display first 5 rows
print("First 5 rows of sales data:\n", df.head())

# Calculate total sales
total_sales = df['Sales'].sum()
print("\nTotal Sales Amount:", total_sales)

# Calculate average sales per region
avg_sales_region = df.groupby('Region')['Sales'].mean()
print("\nAverage Sales Per Region:\n", avg_sales_region)

# Find region with highest average sales
top_region = avg_sales_region.idxmax()
print("\nRegion with Highest Average Sales:", top_region)
