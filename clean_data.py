import pandas as pd

df=pd.read_csv("DataCoSupplyChainDataset.csv",
    encoding="latin1")

print("Original Shape:", df.shape)

#Handle missing values

df["Customer Lname"]=df["Customer Lname"].fillna("Unknown")

df["Customer Zipcode"]=df["Customer Zipcode"].fillna(-1)

#Remove completely empty column

df=df.drop(columns=["Order Zipcode","Product Description"])

#Convert data columns

df["order date (DateOrders)"]=pd.to_datetime(
    df["order date (DateOrders)"],
    errors="coerce"
)

df["shipping date (DateOrders)"]=pd.to_datetime(
    df["shipping date (DateOrders)"],
    errors="coerce"
)

#check duplicates

print("Duplicate rows:", df.duplicated().sum())

#check missing values again

print("\nMissing values after cleaning:")
print(df.isnull().sum())

#final shape

print("\nFinal Shape:", df.shape)

#verify removed columns

print("\nRemaining columns:")
print(df.columns.tolist())



columns_to_remove=[
    "Customer Email",
    "Customer Password",
    "Customer Street",
    "Customer Fname",
    "Customer Lname"
]

df=df.drop(columns=columns_to_remove)

print("\nremoved columns:")
print(columns_to_remove)

print("\nFinal Shape:", df.shape)

df.to_csv("clean_logistics_data.csv", index=False)

print("\nCleaned dataset saved successfully.")