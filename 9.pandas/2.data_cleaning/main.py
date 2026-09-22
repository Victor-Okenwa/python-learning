import pandas as pd

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "Diana"],
    "age": [24, None, 19, 41],
    "score": [85, 72, None, 68]
})

# print(df)
print(df.isna())
print(df.isna().sum())
print(df.dropna())
