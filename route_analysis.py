
import pandas as pd

# Load clustered dataset
df = pd.read_csv("clustered_logistics_data.csv")

# Calculate shipping delay
df["Shipping_Delay"] = (
    df["Days for shipping (real)"]
    - df["Days for shipment (scheduled)"]
)

# Analyze delays by order region
region_analysis = df.groupby("Order Region").agg(
    Total_Orders=("Order Id", "count"),
    Avg_Shipping_Days=("Days for shipping (real)", "mean"),
    Avg_Delay=("Shipping_Delay", "mean"),
    Late_Risk_Rate=("Late_delivery_risk", "mean")
)

region_analysis["Late_Risk_Rate"] *= 100

region_analysis = region_analysis.sort_values(
    "Avg_Delay", ascending=False
)

print("\n===== DELIVERY DELAY BY REGION =====")
print(region_analysis.round(2))

# Save results
region_analysis.to_csv("route_region_analysis.csv")

print("\nRegion analysis saved successfully.")