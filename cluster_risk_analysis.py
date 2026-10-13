
import pandas as pd

# Load clustered dataset
df = pd.read_csv("clustered_logistics_data.csv")

# print(df.columns.tolist())

# Late delivery risk by shipping mode
print("\n===== RISK BY SHIPPING MODE =====")

shipping = df.groupby(["Cluster", "Shipping Mode"]).agg(
    Total_Orders=("Shipping Mode", "size"),
    Late_Risk_Rate=("Late_delivery_risk", "mean")
)

shipping["Late_Risk_Rate"] *= 100
print(shipping.round(2))

# Late delivery risk by order priority
print("\n===== RISK BY ORDER PRIORITY =====")

priority = df.groupby(["Cluster", "Order Status"]).agg(
    Total_Orders=("Order Status", "size"),
    Late_Risk_Rate=("Late_delivery_risk", "mean")
)

priority["Late_Risk_Rate"] *= 100
print(priority.round(2))

# Save results
shipping.to_csv("cluster_shipping_risk.csv")
priority.to_csv("cluster_priority_risk.csv")

print("\nRisk analysis completed successfully.")