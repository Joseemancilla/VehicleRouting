# VehicleRouting
This is my implementation of the Vehicle Routing Problem (VRP) in Python. The code takes in a file containing information about customers, vehicles, and their capacities, and uses a greedy algorithm to assign customers to vehicles in a way that minimizes the total distance traveled by all vehicles. The program first calculates the difference in coordinates between all customer points using the "coor_dif" function, then uses a greedy algorithm to assign customers to vehicles based on their demand. The total cost of the routes is calculated using the "coor_dif" function, and the program returns the final cost and the routes assigned to each vehicle. 
