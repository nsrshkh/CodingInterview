import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

# Vectorized addition
result = a + b  # [11, 22, 33, 44]


# Slow, manual way
result1 = []
for i in range(len(a)):
    result1.append(a[i] + b[i])


# Example with pandas
import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': [5, 6, 7]})

# Vectorized operation: add 10 to all values in 'A'
df['A'] = df['A'] + 10  # [11, 12, 13]