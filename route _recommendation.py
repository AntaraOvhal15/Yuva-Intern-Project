# Route Optimization Summary

baseline_distance = 28.27
nearest_neighbor_distance = 26.47
optimal_distance = 24.73

print("===== Route Optimization Summary =====")

print(f"Baseline Route: {baseline_distance:.2f} km")
print(f"Nearest Neighbor Route: {nearest_neighbor_distance:.2f} km")
print(f"Optimal Route: {optimal_distance:.2f} km")

savings = baseline_distance - optimal_distance
savings_percent = (savings / baseline_distance) * 100

print(f"\nDistance Saved: {savings:.2f} km")
print(f"Distance Reduction: {savings_percent:.2f}%")

print("\n===== Recommendations =====")
print("1. Use the shortest route to reduce travel distance.")
print("2. Optimize delivery stop order before dispatch.")
print("3. Monitor late deliveries using the logistics analysis.")
print("4. Test the route using real road distances before implementation.")