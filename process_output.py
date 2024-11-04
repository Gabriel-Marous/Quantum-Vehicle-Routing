import random

def parse_string(input_string):
    return list(map(int, input_string.split('_')))

def check_feasibility_sample(sample, num_vehicles, num_steps, distances, max_distance, debug=False):

    routes =  [[-1]*num_steps for _ in range(num_vehicles)]

    # Go through all entries
    for key, val in sample.items():
        vehicle, vertex, step = parse_string(key)
        if val == 1.0:
            if routes[vehicle][step] == -1:
                routes[vehicle][step] = vertex
            else:
                # Location visited multiple times
                if debug:
                    print(f"Violated constraint that vehicle {vehicle} can not be at multiple locations at once")
                return False
            
    # Next, check that everything is visited
    visited = [False]*(num_steps+1)

    for route in routes:
        for step in route:
            if step != -1:
                visited[step] = True

    if debug: print(visited)
    
    # Check all locations except depot since there is an implicit start and end visit
    for i in range(1, len(visited)):
        if not visited[i]:
            if debug:
                print(f"Violated constraint that location {i} must be visited")
            return False

    # Finally, check that capacities are respected
    for idx, route in enumerate(routes):
        cost = 0

        if route:
            cost += distances[num_steps][route[0]]
            cost += distances[route[-1]][num_steps]

            for i in range(num_steps - 1):
                cost += distances[route[i]][route[i+1]]

        if cost > max_distance:
            if debug:
                print(f"Violated constraint that vehicle {idx} must travel under {max_distance} distance")
            return False

    return True

def get_routes_from_sample(sample, num_vehicles, num_steps):
    """Builds a set of routes from the sample returned."""

    routes =  [[-1]*num_steps for _ in range(num_vehicles)]

    # Go through all entries
    for key, val in sample.items():
        vehicle, vertex, step = parse_string(key)
        if val == 1.0:
            routes[vehicle][step] = vertex

    # Clean up trailing and leading values (not optimized)
    # for route in routes:
    #     while route:
    #         if route[0] == 5:
    #             route.pop(0)
    #         else:
    #             break
    #     while route:
    #         if route[-1] == 5:
    #             route.pop(len(route) - 1)
    #         else:
    #             break
    
    return routes

def get_cost_routes(paths, distances):
    cost = 0

    num_vertices = len(distances)

    for path in paths:
        if len(path) > 0:

            # Cost in middle of path
            for i in range(len(path) - 1):
                cost += distances[path[i]][path[i+1]]

            # Cost of first choice
            cost += distances[0][path[0]]

            # Cost of last choice
            cost += distances[path[len(path) - 1]][0]

    return cost * 1.0

def report_output(routes, distances):
    print(f'Best routes (depot omitted at start and end):')
    for num, route in enumerate(routes):
        print(f'\tVehicle {num}: {route}')

    print(f'Best cost: {get_cost_routes(routes, distances)}')


def sanity_check(distances, num_vehicles):
    """Test a number of random routes to determine if the outputted score is reasonably good. Quick and lazy indicator of quality"""

    r = []
    for i in range(num_vehicles):
        r.append(i)

    min = 300
    best_route = r
    # Randomly sample a lot of options
    for i in range(10000):
        random.shuffle(r)

        routes = []

        average_visits_per_vehicle = len(distances) // num_vehicles

        for i in range(num_vehicles - 1):
            routes.append(r[i*average_visits_per_vehicle : (i+1)*average_visits_per_vehicle])

        r.append(r[(num_vehicles-1)*average_visits_per_vehicle:])

        cost = get_cost_routes(routes, distances)
        if cost < min:
            min = cost
            best_routes = routes
    print(min)
    print(best_routes)

def lazy_sanity_check(num_destinations, num_vehicles, distances, max_distance):
    """Randomly sample routes, distribute locations evenly between vehicles"""

    locations = []
    for i in range(1, num_destinations + 1):
        locations.append(i)

    min = 300
    best_routes = None
    # Randomly sample a lot of options
    for i in range(10000):
        routes = []
        random.shuffle(locations)

        for i in range(num_vehicles - 1):
            routes.append(locations[i * num_destinations // num_vehicles : (i+1) * num_destinations // num_vehicles])
        
        routes.append(locations[(num_vehicles-1) * num_destinations // num_vehicles:])

        cost = get_cost_routes(routes, distances)
        if cost < min:
            min = cost
            best_routes = routes
    
    return min, best_routes