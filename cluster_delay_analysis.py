
import pandas as pd

# Load clustered dataset
df = pd.read_csv("clustered_logistics_data.csv")

# Calculate delay for each order
df["Shipping_Delay"] = (
    df["Days for shipping (real)"]
    - df["Days for shipment (scheduled)"]
)

# Summarize delivery performance by cluster
summary = df.groupby("Cluster").agg(
    Total_Orders=("Cluster", "size"),
    Avg_Actual_Days=("Days for shipping (real)", "mean"),
    Avg_Scheduled_Days=("Days for shipment (scheduled)", "mean"),
    Avg_Delay=("Shipping_Delay", "mean"),
    Late_Risk_Rate=("Late_delivery_risk", "mean")
)

summary["Late_Risk_Rate"] *= 100

print("\n===== DELAY ANALYSIS BY CLUSTER =====")
print(summary.round(2))

# Save results
summary.to_csv("cluster_delay_summary.csv")

print("\nCluster delay summary saved successfully.")