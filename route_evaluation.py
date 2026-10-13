
import pandas as pd
from itertools import permutations
from math import radians, sin, cos, sqrt, atan2

# Sample locations
df = pd.DataFrame({
    "Location": ["Warehouse", "A", "B", "C", "D"],
    "Latitude": [18.5204, 18.5314, 18.5074, 18.5642, 18.4900],
    "Longitude": [73.8567, 73.8446, 73.8325, 73.7769, 73.8100]
})

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

# Store coordinates for quick lookup
coords = {
    row["Location"]: (row["Latitude"], row["Longitude"])
    for _, row in df.iterrows()
}

def route_distance(route):
    total = 0

    for i in range(len(route) - 1):
        lat1, lon1 = coords[route[i]]
        lat2, lon2 = coords[route[i + 1]]
        total += distance(lat1, lon1, lat2, lon2)

    return total

# Check every possible order of A, B, C, D
delivery_points = ["A", "B", "C", "D"]
results = []

for order in permutations(delivery_points):
    route = ["Warehouse"] + list(order) + ["Warehouse"]
    results.append((route_distance(route), route))

results.sort(key=lambda x: x[0])

# Read the Nearest Neighbor route
nn_df = pd.read_csv("sample_optimized_route.csv")
nn_route = nn_df["Location"].tolist()
nn_distance = route_distance(nn_route)

best_distance, best_route = results[0]

print("===== ROUTE ALGORITHM EVALUATION =====")
print("Nearest Neighbor route:", " -> ".join(nn_route))
print(f"Nearest Neighbor distance: {nn_distance:.2f} km")

print("\nShortest route found:")
print(" -> ".join(best_route))
print(f"Shortest distance: {best_distance:.2f} km")

print(f"\nRoutes evaluated: {len(results)}")
print(f"Extra distance of Nearest Neighbor: "
      f"{nn_distance - best_distance:.2f} km")

print("\n===== TOP 5 ROUTES =====")
for dist, route in results[:5]:
    print(f"{' -> '.join(route)} : {dist:.2f} km")