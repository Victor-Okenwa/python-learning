from pathlib import Path
import pandas as pd

current_dir = Path(__file__).parent
file_path = current_dir / "customers_ai_training.csv"

df = pd.read_csv(file_path)
# print(df)
# print("Head of the dataframe: ", df.head())
# print("Info of the dataframe: ", df.info())
# print("Describe of the dataframe: ", df.describe())
# print("Isna of the dataframe: ", df.isna().sum())
# print("Duplicated of the dataframe: ", df.duplicated().sum())
df["spending"] = pd.to_numeric(df["spending"], errors="coerce")
# print(df["spending"])
df["spending"].isna()
print("--------------------------")
# print(df[df["spending"].isna()])
# print("--------------------------")
# df = df.dropna(subset=["spending"]) # drop the rows where the spending is nan
# df["spending"] = df["spending"].fillna(df["spending"].mean()) # fill the nan with the mean of the spending
# print(df["spending"])

# Exercise
# print(df["spending"].mean())
# df["spending"] = df["spending"].fillna(df["spending"].mean())
# print(df.loc[7])

# df.duplicated().sum()
# print(df[df.duplicated()])

print(df.groupby("country")["spending"].mean()) # Which country has the highest spending?

