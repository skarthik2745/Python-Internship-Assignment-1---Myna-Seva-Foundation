import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, np.nan, 3],
    'B': [np.nan, 5, 6],
    'C': [7, 8, np.nan]
})
missing = df.isnull().sum()
print("Missing values in each column:\n", missing)