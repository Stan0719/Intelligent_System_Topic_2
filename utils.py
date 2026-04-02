import math

def calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def total_route_distance(route, warehouse=(0, 0)):
    if not route:
        return 0

    total = 0
    current = warehouse

    for stop in route:
        total += calculate_distance(current, stop)
        current = stop

    total += calculate_distance(current, warehouse)  # return to warehouse
    return total