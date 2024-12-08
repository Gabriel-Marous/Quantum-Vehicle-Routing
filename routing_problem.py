# Objects for representing all of the details of a routing problem

class RoutingProblem:

    def __init__(self, cost_matrix: list[list[int]], num_vehicles=1, vehicle_capacity=None):
        self.cost_matrix = cost_matrix
        self.num_vehicles = num_vehicles
        self.vehicle_capacity = vehicle_capacity

class RoutingSolution:

    def __init__(self, num_variables, num_constraints, num_biases, samples, time):
        self.num_variables = num_variables
        self.num_constraints = num_constraints
        self.num_biases = num_biases
        self.samples = samples
        self.time = time