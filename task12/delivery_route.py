import math
import itertools

warehouse = (0, 0)
deliveries = [(2,3), (5,4), (8,1), (4,7), (1,8)]

def distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    dx = x2 - x1
    dy = y2 - y1
    res = math.sqrt(dx*dx + dy*dy)
    # or math.hypot(dx, dy) i think this clear than math.sqrt
    return res

def route_distance(route):
    total = 0
    for i in range(len(route) - 1):
        total += distance(route[i], route[i+1])
    return total

def main():
    best_distance = float("inf")
    best_route = None

    for perm in itertools.permutations(deliveries):
        route = [warehouse] + list(perm) + [warehouse]
        current_distance = route_distance(route)

        if current_distance < best_distance:
            best_distance = current_distance
            best_route = route
    print("Shortest Route:", best_route)
    print("Shortest Distance:", round(best_distance, 2))


if __name__ == "__main__":
    main()
