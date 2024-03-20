import pandas as pd
import numpy as np

# Read the input dataset
dataset = pd.read_csv('part_a_input_dataset_1.csv')

# Number of vehicles and maximum capacity per vehicle
num_vehicles = 2
max_capacity = 20

# Extract the depot coordinates
depot_lat = dataset['depot_lat'].iloc[0]
depot_lng = dataset['depot_lng'].iloc[0]


# Calculate distances between nodes using haversine formula
def haversine(lat1, lon1, lat2, lon2):
  R = 6371  # Radius of the Earth in km
  phi1 = np.radians(lat1)
  phi2 = np.radians(lat2)
  delta_phi = np.radians(lat2 - lat1)
  delta_lambda = np.radians(lon2 - lon1)
  a = np.sin(delta_phi /
             2)**2 + np.cos(phi1) * np.cos(phi2) * np.sin(delta_lambda / 2)**2
  res = R * (2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a)))
  return np.round(res, 2)


# Calculate distance matrix between all points
num_points = len(dataset)
distance_matrix = np.zeros((num_points, num_points))
for i in range(num_points):
  for j in range(num_points):
    distance_matrix[i][j] = haversine(dataset['lat'].iloc[i],
                                      dataset['lng'].iloc[i],
                                      dataset['lat'].iloc[j],
                                      dataset['lng'].iloc[j])

# Nearest Neighbor Algorithm for each vehicle
best_routes = []
remaining_points = set(range(1, num_points))  # Exclude the depot
for _ in range(num_vehicles):
  current_point = 0  # Start from the depot
  route = [0]  # Include the depot in the route
  remaining_capacity = max_capacity

  while remaining_points and remaining_capacity > 0:
    nearest_point = min(remaining_points,
                        key=lambda x: distance_matrix[current_point][x])
    if remaining_capacity >= dataset['demand'].iloc[nearest_point]:
      route.append(nearest_point)
      remaining_points.remove(nearest_point)
      remaining_capacity -= dataset['demand'].iloc[nearest_point]
      current_point = nearest_point
    else:
      break

  route.append(0)  # Return to the depot
  best_routes.append(route)

# Output the best routes
for i, vehicle_route in enumerate(best_routes):
  print(f"Vehicle {i + 1} delivery route:")
  for j, point in enumerate(vehicle_route):
    order_id = dataset['order_id'].iloc[point]
    print(
        f"{order_id} - {dataset['lng'].iloc[point]}, {dataset['lat'].iloc[point]}"
    )
  print(
      f"Total distance: {sum(distance_matrix[point1][point2] for point1, point2 in zip(vehicle_route[:-1], vehicle_route[1:]))} kms"
  )

# Write the output to CSV
output_rows = []
for i, vehicle_route in enumerate(best_routes):
  for j, point in enumerate(vehicle_route):
    order_id = dataset['order_id'].iloc[point]
    lng = dataset['lng'].iloc[point]
    lat = dataset['lat'].iloc[point]
    output_rows.append({
        'order_id': order_id,
        'lng': lng,
        'lat': lat,
        'depot_lat': depot_lat,
        'depot_lng': depot_lng,
        'vehicle_num': i + 1,
        'dlvr_seq_num': j + 1
    })

output_df = pd.concat([pd.DataFrame([row]) for row in output_rows],
                      ignore_index=True)
output_df.to_csv('part_a_output_dataset_1.csv', index=False)
