import pandas as pd

# Series
series = pd.Series([25, 31, 22, 28, "Hello"])
# print(series)

# DataFrame
data = {
    "name": ["John", "Jane", "Jim", "Jill"],
    "age": [25, 31, 22, 28],
    "country": ["Nigeria", "Ghana", "Kenya", "Nigeria"],
    "spending": [120, 250, 90, 180]
}
df = pd.DataFrame(data)
# print("DataFrame:", df)
# print(df["name"])
# print(df[["name", "age"]])

# print("Head:", df.head())
# print("Tail:", df.tail())
# print("info:", df.info())
# print("describe:", df.describe())
# print("describe:", df["age"] > 25)
# print("describe:", df[
#     (df["country"] == "Nigeria") &
#     (df["age"] >= 25)
# ])
#  When working with pandas & mens AND while | means OR


# Exercise 

data = {
    "name": ["Alice", "Bob", "Charlie", "Diana", "Evan"],
     "age": [24, 32, 19, 41, 27],
    "score": [85, 72, 91, 68, 88],
    "country": ["Nigeria", "Ghana", "Nigeria", "Kenya", "Ghana"]
}
df = pd.DataFrame(data)
print(df.head(2))
print(df.tail(2))
# print(df.info())
# print(df["name"])
# print(df[["name", "score"]])
# print(df[["name", "age"]][ "age"] > 25)
print(df[df["country"] == "Nigeria"])
# print(df[
#  (df["country"] == "Nigeria") &
#  (df["age"] > 25)
# ])