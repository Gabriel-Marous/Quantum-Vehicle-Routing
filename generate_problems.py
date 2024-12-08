# Generate a common set of problems on which to benchmark results
# For now use random entries where triangle inequality is guarenteed
# This could later be imporved with real-world data

import random
random.seed(7)

import pickle

from routing_problem import RoutingProblem

problem_sizes = [5*i for i in range(1, 7)]
num_vehicles = [i for i in range(1, 7)]
max_distance = [60]*6
examples = 3

for locations, vehicles, capacity in zip(problem_sizes, num_vehicles, max_distance):
    for v in range(examples):

        cost_matrix = [[0]*(locations+1) for _ in range(locations+1)]

        for i in range(locations + 1):
            for j in range(i, locations + 1):
                if i == j:
                    cost_matrix[i][j] = 0
                else:
                    val = random.randint(5, 9)
                    cost_matrix[i][j] = val
                    cost_matrix[j][i] = val

        problem = RoutingProblem(cost_matrix, vehicles, capacity)

        file_name = f"routing_problems/vrp_{vehicles}m_{locations}n_{capacity}c_v{v}.pkl"

        with open(file_name, "wb") as out:
            pickle.dump(problem, out, pickle.HIGHEST_PROTOCOL)

        




