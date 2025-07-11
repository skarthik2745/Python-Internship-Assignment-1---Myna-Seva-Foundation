import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Student': ['Tom', 'Jerry', 'Spike'],
    'Marks': [75, 89, 67]
})
df['Top Scorer'] = np.where(df['Marks'] == df['Marks'].max(), '🏆', '')
print(df)