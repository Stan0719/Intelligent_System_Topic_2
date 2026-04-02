import math

def euclidean_distance(point1, point2):
    x1, y1 = point1[1], point1[2]
    x2, y2 = point2[1], point2[2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def route_distance(start, route):
    total = 0
    current = start

    for stop in route:
        total += euclidean_distance(current, stop)
        current = stop

    total += euclidean_distance(current, start)   # return to warehouse
    return total