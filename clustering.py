import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

df = pd.read_csv("clean_logistics_data.csv")
print(df.shape)

features = [
    "Days for shipping (real)",
    "Days for shipment (scheduled)",
    "Product Price",
    "Order Item Quantity"
]

features = [
    col for col in features if col in df.columns
]
#prepare the data 

cluster_df = df[features].dropna().copy()

print(cluster_df.shape)

#scale the feature

scaler=StandardScaler()
scaled_data=scaler.fit_transform(cluster_df)

#create k-means model

kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

# assign cluster label 

cluster_df["Cluster"]=kmeans.fit_predict(scaled_data)

#understand cluster summary

kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

# count ordeer in each cluster

print(cluster_df["Cluster"].value_counts().sort_index)

#save the clusters result

print(
    cluster_df["Cluster"].value_counts().sort_index()
)


# Cluster characteristics
print("\n===== CLUSTER SUMMARY =====")

summary = cluster_df.groupby("Cluster")[features].mean().round(2)

print(summary)


# Analyze late deliveries by cluster

analysis_df = df.loc[cluster_df.index].copy()
analysis_df["Cluster"] = cluster_df["Cluster"]

print("\n===== LATE DELIVERY RATE BY CLUSTER =====")

late_summary = analysis_df.groupby("Cluster").agg(
    Total_Orders=("Late_delivery_risk", "count"),
    Late_Orders=("Late_delivery_risk", "sum")
)

late_summary["Late_Delivery_Rate"] = (
    late_summary["Late_Orders"]
    / late_summary["Total_Orders"] * 100
).round(2)

print(late_summary)


# Verify actual delivery status by cluster

analysis_df = df.loc[cluster_df.index].copy()
analysis_df["Cluster"] = cluster_df["Cluster"]

print("\n===== ACTUAL DELIVERY STATUS BY CLUSTER =====")

print(
    pd.crosstab(
        analysis_df["Cluster"],
        analysis_df["Delivery Status"],
        normalize="index"
    ).mul(100).round(2)
)


status_summary = pd.crosstab(
    analysis_df["Cluster"],
    analysis_df["Delivery Status"],
    normalize="index"
).mul(100).round(2)

print("\n===== COMPLETE DELIVERY STATUS ANALYSIS =====")
print(status_summary.to_string())

# Save clustered dataset
df.loc[cluster_df.index, "Cluster"] = cluster_df["Cluster"]

df.to_csv("clustered_logistics_data.csv", index=False)

print("Clustering results saved successfully.")
