import pandas as pd
import numpy as np

# Create product data
data = {
    "Product": ["Pen", "Notebook", "Eraser", "Pencil"],
    "Price": [10, 40, 5, 7],
    "Quantity": [100, 50, 200, 150]
}

df = pd.DataFrame(data)

print("Sales Data:\n", df)

# Calculate total amount
df["Total"] = df["Price"] * df["Quantity"]

# Apply 10% discount using NumPy
df["Discounted Total"] = df["Total"] * np.where(df["Total"] > 500, 0.9, 1.0)

print("\nAfter Applying Discount:\n", df)