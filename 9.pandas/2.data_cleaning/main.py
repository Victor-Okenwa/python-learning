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

# print(df.duplicated())
# print(df.drop_duplicates())


# Data Types & Conversions

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie"],
    "age": ["24", "32", "unknownw"],
    "score": ["85", "72", "91"]
})

df["age"] = pd.to_numeric(df["age"], errors="coerce")
df["score"] = pd.to_numeric(df["score"], errors="coerce")

# print(df.dtypes)
# print(df)


#  GROUPING DATA
df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "country": ["Nigeria", "Ghana", "Nigeria", "Ghana", "Nigeria"],
    "score": [85, 72, 91, 68, 78]
})

# print(df.groupby("country")["score"].mean())

# APPLYING TRANSFORMATIONS

df["score_percent"] = df["score"] / 100
df["name_length"] = df["name"].apply(len)

print(df)

# EXERCISE
df["passed"] = df["score"] >= 50
print(df)