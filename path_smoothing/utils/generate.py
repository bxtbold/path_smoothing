import random


def generate_control_points(dimension, point_number, should_x_sequantial=True):
    data = []
    for _ in range(dimension):
        data.append([random.randint(-10, 10) for _ in range(point_number)])

    if should_x_sequantial:
        for i in range(point_number):
            data[0][i] = i
    return data
