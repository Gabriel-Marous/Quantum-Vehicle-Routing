# Test a variety of scales of problems
# Input the type of solver to test on the benchmark: (default, path_efficient)

from vrp import *
from routing_problem import RoutingProblem, RoutingSolution
from credentials import TOKEN
import time
import pickle
import random
random.seed(7)

solvers = {'default': DefaultRoutingModel, 'bounded_path': BoundedPathModel}

# Process the input, get the solver to use
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("solver", type=str, help="Name of QUBO solver to use ('default', 'path_efficient')")
args = parser.parse_args()
solver = args.solver
assert solver in solvers

print(f"Using {solver} solver\n")


for m in range(1, 7):
    for v in range(3):

        instance_str = f'vrp_{m}m_{5*m}n_{60}c_v{v}'

        print(f"Running {instance_str}")

        # Unpack the saved problem instance
        with open(f'routing_problems/{instance_str}.pkl', 'rb') as file:
            problem = pickle.load(file)

        # Create the solver
        model = solvers[solver](
            num_locations = len(problem.cost_matrix) - 1, 
            distances = problem.cost_matrix, 
            num_vehicles = problem.num_vehicles, 
            max_distance = problem.vehicle_capacity
        )
        model.build_constrained_model()

        # Run the model and save the 
        t1 = time.time()
        sample = model.run_constrained_model(TOKEN)
        t2 = time.time()

        solution = RoutingSolution(
            num_variables = len(model.x),
            num_constraints = len(model.cqm.constraints),
            num_biases = model.cqm.num_biases(),
            samples = sample,
            time = t2 - t1
        )

        with open(f'results/{solver}/{instance_str}.pkl', 'wb') as out:
            pickle.dump(solution, out, pickle.HIGHEST_PROTOCOL)




