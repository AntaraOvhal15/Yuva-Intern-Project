
# import pandas as pd

# df = pd.read_csv("clustered_logistics_data.csv")

# print("===== LOCATION DATA VALIDATION =====")

# # Check missing coordinates
# print("\nMissing latitude values:", df["Latitude"].isna().sum())
# print("Missing longitude values:", df["Longitude"].isna().sum())

# # Display country and coordinate combinations
# print("\n===== SAMPLE LOCATION RECORDS =====")
# print(
#     df[[
#         "Order Country",
#         "Order City",
#         "Latitude",
#         "Longitude"
#     ]].drop_duplicates().head(20).to_string(index=False)
# )

# # Check coordinate ranges
# invalid = df[
#     ~df["Latitude"].between(-90, 90)
#     | ~df["Longitude"].between(-180, 180)
# ]

# print("\nRecords with invalid coordinate ranges:", len(invalid))

# # Save records for review
# invalid.to_csv("invalid_coordinates.csv", index=False)

# print("\nValidation completed.")


import pandas as pd

df = pd.read_csv("clean_logistics_data.csv")

print("===== CUSTOMER LOCATION SAMPLE =====")
print(
    df[[
        "Customer Country",
        "Customer City",
        "Latitude",
        "Longitude"
    ]].drop_duplicates().head(20).to_string(index=False)
)

print("\n===== ORDER LOCATION SAMPLE =====")
print(
    df[[
        "Order Country",
        "Order City",
        "Latitude",
        "Longitude"
    ]].drop_duplicates().head(20).to_string(index=False)
)
