
import pandas as pd

df = pd.read_csv("clustered_logistics_data.csv")

# Calculate shipping delay
df["Shipping_Delay"] = (
    df["Days for shipping (real)"]
    - df["Days for shipment (scheduled)"]
)

# Analyze by country and city
city_analysis = df.groupby(
    ["Order Country", "Order City"]
).agg(
    Total_Orders=("Order Id", "count"),
    Avg_Delay=("Shipping_Delay", "mean"),
    Late_Risk_Rate=("Late_delivery_risk", "mean"),
    Latitude=("Latitude", "mean"),
    Longitude=("Longitude", "mean")
).reset_index()

# Keep locations with at least 100 orders
city_analysis = city_analysis[
    city_analysis["Total_Orders"] >= 100
].copy()

city_analysis["Late_Risk_Rate"] *= 100

# Sort by highest average delay
city_analysis = city_analysis.sort_values(
    "Avg_Delay", ascending=False
)

print("\n===== TOP 15 HIGH-DELAY LOCATIONS =====")
print(city_analysis.head(15).round(2))

city_analysis.head(15).to_csv(
    "high_delay_locations.csv", index=False
)

print("\nHigh-delay locations saved successfully.")


print("\n===== CHECK LOCATION COORDINATES =====")

print(
    df[[
        "Order Country",
        "Order City",
        "Latitude",
        "Longitude"
    ]].head(10).to_string(index=False)
)

print("\n===== CHECK HIGH-DELAY LOCATIONS =====")

print(
    city_analysis[[
        "Order Country",
        "Order City",
        "Latitude",
        "Longitude",
        "Total_Orders",
        "Avg_Delay"
    ]].head(15).to_string(index=False)
)