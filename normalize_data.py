import pandas as pd
from sklearn.preprocessing import MinMaxScaler

#load a cleaned dataset

df=pd.read_csv("clean_logistics_data.csv")
 
print("Original Shape:",df.shape)

#numerical feature selected for normalization

normalization_columns=[
    "Sales",
    "Order Item Total",
    "Order Profit Per Order",
    "Product Price",
    "Order Item Discount"
]

#create scaler
scaler = MinMaxScaler()

#Apply Min-Max normalization
df[normalization_columns]=scaler.fit_transform(df[normalization_columns])

print("\n=====Normalized data=====")
print(df[normalization_columns].head())

print("\n=====Minimun values=====")
print(df[normalization_columns].min())

print("\n=====Maximun values=====")
print(df[normalization_columns].max())

#save normalized dataset

df.to_csv(
    "normalized_logistics_data.csv",index=False
)

print("\nNormalized dataset saved successfully.")