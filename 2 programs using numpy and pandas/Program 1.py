import pandas as pd
import numpy as np

# Create a simple DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Math": [85, 78, 92, 70],
    "Science": [90, 76, 88, 80],
    "English": [75, 85, 78, 82]
}

df = pd.DataFrame(data)

print("Student Marks Data:\n", df)

# Calculate average marks
df["Average"] = df[["Math", "Science", "English"]].mean(axis=1)

# Find student with highest and lowest average
highest = df.loc[df["Average"].idxmax()]
lowest = df.loc[df["Average"].idxmin()]

print("\nWith Average:\n", df)
print("\nTopper:\n", highest)
print("\nLowest Scorer:\n", lowest)