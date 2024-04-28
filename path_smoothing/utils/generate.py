import random


def generate_control_points(dimension, point_number):
    data = []
    for _ in range(dimension):
        data.append([random.randint(-10, 10) for _ in range(point_number)])

    return data
