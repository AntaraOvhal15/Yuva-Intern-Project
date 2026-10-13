
import pandas as pd
from math import radians, sin, cos, sqrt, atan2

# Sample locations for demonstration only
locations = pd.DataFrame({
    "Location": ["Warehouse", "A", "B", "C", "D"],
    "Latitude": [18.5204, 18.5314, 18.5074, 18.5642, 18.4900],
    "Longitude": [73.8567, 73.8446, 73.8325, 73.7769, 73.8100]
})

# Calculate straight-line distance in kilometers
def distance(lat1, lon1, lat2, lon2):
    radius = 6371

    lat1, lon1, lat2, lon2 = map(
        radians, [lat1, lon1, lat2, lon2]
    )

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = (
        sin(dlat / 2) ** 2
        + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    )

    return 2 * radius * atan2(sqrt(a), sqrt(1 - a))


# Nearest Neighbor route
unvisited = list(range(1, len(locations)))
route = [0]
total_distance = 0

while unvisited:
    current = route[-1]

    nearest = min(
        unvisited,
        key=lambda i: distance(
            locations.loc[current, "Latitude"],
            locations.loc[current, "Longitude"],
            locations.loc[i, "Latitude"],
            locations.loc[i, "Longitude"]
        )
    )

    total_distance += distance(
        locations.loc[current, "Latitude"],
        locations.loc[current, "Longitude"],
        locations.loc[nearest, "Latitude"],
        locations.loc[nearest, "Longitude"]
    )

    route.append(nearest)
    unvisited.remove(nearest)

# Return to warehouse
current = route[-1]
total_distance += distance(
    locations.loc[current, "Latitude"],
    locations.loc[current, "Longitude"],
    locations.loc[0, "Latitude"],
    locations.loc[0, "Longitude"]
)
route.append(0)

print("===== SAMPLE ROUTE OPTIMIZATION =====")
print(" -> ".join(locations.loc[i, "Location"] for i in route))
print(f"Total straight-line distance: {total_distance:.2f} km")

locations.iloc[route].to_csv(
    "sample_optimized_route.csv", index=False
)

print("Sample route saved successfully.")