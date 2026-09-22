import pandas as pd

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "Diana"],
    "age": [24, None, 19, 41],
    "score": [85, 72, None, 68]
})

df["age"] = df["age"].fillna(df["age"].mean())
df["score"] = df["score"].fillna(df["score"].mean())
# print(df)
# print(df.isna())
# print(df.isna().sum())
# print(df.dropna())


# EXERCISE
df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "Diana", "Evan"],
    "age": [24, None, 19, 41, None],
    "score": [85, 72, None, 68, 88],
    "country": ["Nigeria", "Ghana", "Nigeria", None, "Ghana"]
})

# print(df.isna().sum())
newdf =  df.dropna()
df["age"] = df["age"].fillna(df["age"].mean())


#  DUPLICATES
df = pd.DataFrame({
    "name": ["Alice", "Bob", "Alice", "Charlie", "Bob"],
    "age": [24, 32, 24, 19, 32],
    "score": [85, 72, 85, 91, 72]
})

print(df.duplicated())
print(df.drop_duplicates())