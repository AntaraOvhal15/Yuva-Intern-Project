import pandas as pd

df = pd.read_csv(
    "DataCoSupplyChainDataset.csv",
    encoding="latin1"
)

print("Dataset Shape:", df.shape)

#numerical columns imp for logistics analysis

columns = [
    "Days for shipping (real)",
    "Days for shipment (scheduled)",
    "Sales",
    "Order Item Total",
    "Order Profit Per Order",
    "Order Item Quantity",
    "Product Price",
    "Order Item Product Price",
    "Order Item Discount"
]

print("\n===== Numerical Statistics =====")

print(df[columns].describe().T)

print("\n=====Invalid Values=====")

print("Negative Sales:",
      (df["Sales"]<0).sum())

print("Negative Quantity:",
      (df["Order Item Quantity"]<0).sum())

print("Negative Product Price:",
      (df["Product Price"]<0).sum())

print("Negative Shipping days:",
      (df["Days for shipping (real)"]<0).sum())

print("\n=====Outlier Analysis=====")

outliers_columns=[
        "Sales",
        "Order Item Total",
        "Order Profit Per Order",
        "Product Price",
        "Order Item Discount"
]

for col in outliers_columns:

    Q1=df[col].quantile(0.25)
    Q3=df[col].quantile(0.75)

    IQR=Q3-Q1

    lower_limit=Q1-1.5*IQR
    upper_limit=Q3+1.5*IQR

    outliers=df[
        (df[col]<lower_limit)|
        (df[col]>upper_limit)       
    ]

    print("\nColumns:", col)
    print("Lower Limit:",lower_limit)
    print("Upper Limit:",upper_limit)
    print("Number of Outliers:",len(outliers))


print("\n===== Extreme Values =====")

for col in outliers_columns:
    print("\nColumn:",col)
    print("Top 10 Values:")
    print(df[col].nlargest(10).tolist())


print("\n===== Outlier Handling Decision =====")
print("Potential outliers were identified using the IQR method.")
print("Extreme values were inspected and found to be plausible business values.")
print("Therefore, the identified outliers were retained.")