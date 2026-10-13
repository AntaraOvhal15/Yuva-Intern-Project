import pandas as pd

#load cleaned dataset

df=pd.read_csv("clean_logistics_data.csv")

print("=====Dataset overview=====")

print("Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nDatatypes:")
print(df.dtypes)

print("\n=====Descriptive statistics=====")

numerical_columns=[
    "Days for shipping (real)",
    "Days for shipment (scheduled)",
    "Sales",
    "Order Item Total",
    "Order Profit Per Order",
    "Order Item Quantity",
    "Product Price",
    "Order Item Discount"
]

print(df[numerical_columns].describe())

print("\n=====Median=====")

print(df[numerical_columns].median())

print("\n=====Mode=====")

print(df[numerical_columns].mode().iloc[0])

print("\n=====Correlation=====")

print(df[numerical_columns].corr())


#visualization

import matplotlib.pyplot as plt

#shipping time comparision

actual_shipping=df["Days for shipping (real)"].mean()
scheduled_shipping=df["Days for shipment (scheduled)"].mean()

labels=["Actual Shippig", "Scheduled Shippng"]
values=[actual_shipping,scheduled_shipping]

plt.figure(figsize=(8,5))
plt.bar(labels,values)
plt.title("Average Actual vs Scheduled Shipping Days")
plt.xlabel("Shipping Type")
plt.ylabel("Average Days")
plt.show()

#Delivery status Distribution

delivery_status=df["Delivery Status"].value_counts()

print("\n=====Delivery Status Count=====")
print(delivery_status)

plt.figure(figsize=(8,5))
delivery_status.plot(kind="bar")

plt.title("Distribution of Delivery Status")
plt.xlabel("Delivery Status")
plt.ylabel("Number of Orders")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


# Sales Distribution Histogram

plt.figure(figsize=(8,5))

plt.hist(df["Sales"], bins=30)

plt.title("Distribution of Sales")
plt.xlabel("Sales")
plt.ylabel("Number of Orders")

plt.tight_layout()
plt.show()


# ===== Sales by Shipping Mode =====

sales_by_shipping = df.groupby("Shipping Mode")["Sales"].sum()

print("\n===== Sales by Shipping Mode =====")
print(sales_by_shipping)

plt.figure(figsize=(8, 5))

sales_by_shipping.plot(kind="bar")

plt.title("Total Sales by Shipping Mode")
plt.xlabel("Shipping Mode")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# ===== Sales vs Product Price =====

plt.figure(figsize=(8, 5))

plt.scatter(
    df["Product Price"],
    df["Sales"],
    alpha=0.3
)

plt.title("Sales vs Product Price")
plt.xlabel("Product Price")
plt.ylabel("Sales")

plt.tight_layout()
plt.show()

# ===== Correlation Heatmap =====

import seaborn as sns

plt.figure(figsize=(10, 7))

sns.heatmap(
    df[numerical_columns].corr(),
    annot=True,
    fmt=".2f",
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")

plt.tight_layout()
plt.show()

# KEy KPIS

#1.On time delivery rate
on_time_rate=(df["Late_delivery_risk"]==0).mean()*100

#2.Late Delivery rate
late_delivery_rate=(df["Late_delivery_risk"]==1).mean()*100

#3.Average Actual shipping days
avg_actual_shipping=df["Days for shipping (real)"].mean()

#4.Average shipping Delay
df["Shipping Delay"]=(
    df["Days for shipping (real)"]
    -df["Days for shipment (scheduled)"]
)

avg_shipping_delay=df["Shipping Delay"].mean()

#5.Total order profit

total_profit=df["Order Profit Per Order"].sum()


# Display KPIs
print(f"\n1. On-Time Delivery Rate     : {on_time_rate:.2f}%")
print(f"2. Late Delivery Rate        : {late_delivery_rate:.2f}%")
print(f"3. Average Actual Shipping   : {avg_actual_shipping:.2f} days")
print(f"4. Average Shipping Delay    : {avg_shipping_delay:.2f} days")
print(f"5. Total Order Profit        : {total_profit:,.2f}")





#Late delivery analysis by shipping mode

late_by_shipping=df.groupby("Shipping Mode").agg(
    Total_Orders=("Shipping Mode","count"),
    Late_Orders=("Late_delivery_risk","sum")
)

late_by_shipping["Late_delivery_Rate"]=(
    late_by_shipping["Late_Orders"]
    / late_by_shipping["Total_Orders"]
)*100

print("\n===== Late Delivery Rate by Shipping Mode =====")
print(late_by_shipping.sort_values("Late_delivery_Rate", ascending=False))

#late delivery analysis by market

late_by_market=df.groupby("Market").agg(
    Total_Orders=("Shipping Mode","count"),
    Late_Orders=("Late_delivery_risk","sum"),
    Total_Sales=("Sales","sum"),
    Total_Profit=("Order Profit Per Order","sum")
)

late_by_market["Late_delivery_Rate"]=(
    late_by_market["Late_Orders"]
    / late_by_market["Total_Orders"]
)*100

print("\n===== Late Delivery Analysis by Market =====")
print(
    late_by_market.sort_values(
        "Late_delivery_Rate",
        ascending=False
    )
)

#Region wise delivery analysis

region_analysis = df.groupby("Order Region").agg(
    Total_Orders=("Order Region", "count"),
    Late_Orders=("Late_delivery_risk", "sum"),
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Order Profit Per Order", "sum")
)

region_analysis["Late_delivery_Rate"] = (
    region_analysis["Late_Orders"]
    / region_analysis["Total_Orders"]
) * 100

print("\n===== Region-wise Delivery Analysis =====")
print(
    region_analysis.sort_values(
        "Late_delivery_Rate",
        ascending=False
    )
)

# shipping delays 

delay_by_region = df.groupby("Order Region").agg(
    Average_Delay=("Shipping Delay", "mean"),
    Maximum_Delay=("Shipping Delay", "max"),
    Total_Orders=("Order Region", "count")
)

print("\n===== Shipping Delay by Region =====")
print(
    delay_by_region.sort_values(
        "Average_Delay",
        ascending=False
    )
)

# high risk analysis

high_risk_region=region_analysis[region_analysis["Late_delivery_Rate"]>50]

print("\n High Risk Region")
print(high_risk_region.sort_values(
    "Late_delivery_Rate",
    ascending=False
))

#Category  wise analysis

category_analysis = df.groupby("Category Name").agg(
    Total_Orders=("Category Name", "count"),
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Order Profit Per Order", "sum"),
    Average_Profit=("Order Profit Per Order", "mean")
)

print("\n===== Category-wise Sales and Profit =====")
print(
    category_analysis.sort_values(
        "Total_Sales",
        ascending=False
    )
)

#Top 10 categories by sales

top_sales_categories = (
    category_analysis["Total_Sales"]
    .sort_values(ascending=False)
    .head(10)
)

print("\n===== Top 10 Categories by Sales =====")
print(top_sales_categories)

plt.figure(figsize=(10, 6))

top_sales_categories.sort_values().plot(kind="barh")

plt.title("Top 10 Product Categories by Sales")
plt.xlabel("Total Sales")
plt.ylabel("Category")

plt.tight_layout()
plt.show()

#Top 10 categories by profit

top_profit_categories = (
    category_analysis["Total_Profit"]
    .sort_values(ascending=False)
    .head(10)
)

print("\n===== Top 10 Categories by Profit =====")
print(top_profit_categories)

plt.figure(figsize=(10, 6))

top_profit_categories.sort_values().plot(kind="barh")

plt.title("Top 10 Product Categories by Profit")
plt.xlabel("Total Profit")
plt.ylabel("Category")

plt.tight_layout()
plt.show()

#category wise late delivery analysis

category_delivery = df.groupby("Category Name").agg(
    Total_Orders=("Category Name", "count"),
    Late_Orders=("Late_delivery_risk", "sum")
)

category_delivery["Late_Delivery_Rate"] = (
    category_delivery["Late_Orders"]
    / category_delivery["Total_Orders"]
) * 100

print("\n===== Category-wise Late Delivery Rate =====")
print(
    category_delivery.sort_values(
        "Late_Delivery_Rate",
        ascending=False
    )
)

