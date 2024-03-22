**Algorithm Used: Nearest Neighbor Algorithm**

1. **High-Level Explanation:**
   - Start from the depot and select the closest customer as the next stop for each vehicle until the vehicle's capacity is reached or all customers are visited.
   - Repeat this process for each vehicle, ensuring that each customer is visited exactly once.
   - Finally, return to the depot to complete the route for each vehicle.

2. **Time Complexity:**
   - The time complexity of the Nearest Neighbor Algorithm is O(n^2), where n is the number of customers (excluding the depot).
   - This is because for each customer, we need to find the nearest neighbor among the remaining customers, which requires comparing distances between each pair of customers.

3. **Space Complexity:**
   - The space complexity of the Nearest Neighbor Algorithm is O(n), where n is the number of customers.
   - This is because we need to store the distance matrix between each pair of customers, which requires O(n^2) space, and additional space for storing the route and other variables.

**Different Algorithms for Different Datasets:**

If different algorithms were used for different datasets in Part A, the explanations would be as follows:

1. **For Dataset 1: Nearest Neighbor Algorithm**
   - **High-Level Explanation:** Same as described above.
   - **Time Complexity:** O(n^2)
   - **Space Complexity:** O(n)

2. **For Dataset 2: Insertion Heuristic Algorithm**
   - **High-Level Explanation:** Start with a route containing only the depot. At each step, insert the customer at the most appropriate position in the route to minimize the total distance. Repeat this process until all customers are visited.
   - **Time Complexity:** O(n^2)
   - **Space Complexity:** O(n)

3. **For Dataset 3: Clarke-Wright Savings Algorithm**
   - **High-Level Explanation:** Calculate the savings achieved by combining each pair of customers' routes into a single route. Merge routes with the highest savings until all customers are visited.
   - **Time Complexity:** O(n^2)
   - **Space Complexity:** O(n)

These algorithms were chosen based on the characteristics of each dataset and their performance in minimizing total distance traveled by the vehicles.

*Part-2*

Algorithm Used: Nearest Neighbor Algorithm
Time Complexity: O(n^2)
Space Complexity: O(n^2)
1. **Nearest Neighbor Algorithm**:
   - **High-level Explanation**: The Nearest Neighbor Algorithm is a constructive heuristic used to find a short path for the Traveling Salesman Problem (TSP). It starts from a designated starting point (the depot in this case) and repeatedly selects the nearest unvisited point until all points are visited, forming a closed loop. In this implementation, the algorithm is applied separately for each vehicle, with each vehicle starting from the depot and making deliveries until it reaches its capacity limit or all deliveries are made.
   - **Time Complexity**: The time complexity of the Nearest Neighbor Algorithm is \(O(n^2)\), where \(n\) is the number of points (orders) in the dataset. This is because for each point, the algorithm needs to find the nearest neighbor, resulting in \(n\) iterations with \(O(n)\) operations each.
   - **Space Complexity**: The space complexity is also \(O(n^2)\) because of the distance matrix that needs to be computed and stored, which has dimensions \(n \times n\), where \(n\) is the number of points.

2. **Variations in Algorithms for Different Datasets**:
   - **If different algorithms were used for different datasets**, we would need to provide separate explanations for each algorithm:
     - **Algorithm 1**: Nearest Neighbor Algorithm
       - **High-level Explanation**: Same as described above.
       - **Complexity**: Time complexity \(O(n^2)\), space complexity \(O(n^2)\).
     - **Algorithm 2**: Clarke-Wright Savings Algorithm
       - **High-level Explanation**: The Clarke-Wright Savings Algorithm is another heuristic used for solving the Vehicle Routing Problem. It constructs routes by merging individual routes that are close to each other and have high savings in distance. It starts with each node (order) as a separate route and then iteratively merges them to optimize the total distance.
       - **Complexity**: Time complexity depends on the implementation but typically ranges from \(O(n^2 \log n)\) to \(O(n^3)\), while space complexity is \(O(n^2)\) to store the distance matrix.
       - **Note**: If different algorithms were used, it would be important to analyze the characteristics of each dataset (size, distribution of points, etc.) to choose the most appropriate algorithm. Additionally, the actual time and space complexities may vary depending on the specific implementation and optimizations applied.
