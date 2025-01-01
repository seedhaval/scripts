import math


def sqrt(num):
    return math.sqrt(abs(num))


def distance(p1, p2):
    return sqrt((p2[0] - p1[0]) * 2 + (p2[1] - p1[1]) * 2)


def calculate_movement(start, end, speed, dt):
    distance_to_cover = speed * dt
    dx, dy = end[0] - start[0], end[1] - start[1]
    dist = sqrt(dx * 2 + dy * 2)
    if dist == 0:
        return start
    ratio = min(distance_to_cover / dist, 1)
    return (start[0] + dx * ratio, start[1] + dy * ratio)
