import pandas as pd

df = pd.DataFrame({
    'A': [1, 2, None, 4],
    'B': [None, 2, 3, 4]
})

print(df.isnull())
# Returns a DataFrame of True/False values for missing entries

print(df.isnull().sum())
# Returns the count of missing values per column

print(df.info())
# Shows number of non-null entries per column