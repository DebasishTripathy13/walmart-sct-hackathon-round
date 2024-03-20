import pandas as pd
import math

# Function to calculate the haversine distance between two points
def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0  # Radius of the Earth in kilometers
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = R * c
    return distance

# Read input data from CSV file
data = pd.read_csv('dataset_part1/part_a_input_dataset_4.csv')

# Initialize variables
n = len(data)
unvisited = set(range(1, n))
current_city = 0
best_route = [0]
best_distance = 0

# Find nearest neighbor for each city
while unvisited:
    nearest_city = min(unvisited, key=lambda x: haversine(data.loc[current_city, 'lat'], data.loc[current_city, 'lng'],
                                                           data.loc[x, 'lat'], data.loc[x, 'lng']))
    best_distance += haversine(data.loc[current_city, 'lat'], data.loc[current_city, 'lng'],
                               data.loc[nearest_city, 'lat'], data.loc[nearest_city, 'lng'])
    current_city = nearest_city
    unvisited.remove(nearest_city)
    best_route.append(nearest_city)

# Add return to depot
best_distance += haversine(data.loc[current_city, 'lat'], data.loc[current_city, 'lng'],
                           data.loc[0, 'lat'], data.loc[0, 'lng'])
best_route.append(0)

# Write output to CSV file
output_data = data.loc[best_route[:-1]]  # Exclude the last 0 (depot)
output_data['dlvr_seq_num'] = range(1, len(output_data) + 1)
output_data.to_csv('part_a_output_dataset_1.csv', index=False)

# Write the best route distance to file
with open('part_a_best_routes_distance_travelled.csv', 'w') as f:
    f.write(f"Dataset,Best Route Distance\npart_a_input_dataset_1,{best_distance} kms\n")

# Print the best route and total distance
print("Best Delivery Route:")
print(" -> ".join(str(data.loc[node, 'order_id']) for node in best_route))
print("Total Distance Travelled:", best_distance, "kms")
