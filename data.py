import pandas as pd
import numpy as np

df=pd.read_csv("DataCoSupplyChainDataset.csv",encoding="latin1")

print("First 5 row:")
print(df.head())

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nData Types")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

print("\nSTatistics:")
print(df.describe())

# print(df.info())
