#! /usr/bin/python
import matplotlib.pyplot as plt
import numpy as np
import random

from cubic_spline import CubicSpline


def compute_spline(*args):
    position = args[:-1]
    ds = args[-1]

    sp = CubicSpline(*position)
    s = np.arange(0, sp.s[-1], ds)

    data = [[] for _ in range(len(position) + 2)]

    for i_s in s:
        position = sp.compute_position(i_s)
        orientation = sp.compute_orientation(i_s)
        curvature_k = sp.compute_curvature(i_s)

        for i in range(len(position)):
            data[i].append(position[i])
        data[-2].append(orientation)
        data[-1].append(curvature_k)

    data.extend([s])

    return data


def generate_data(dimension, point_number):
    data = []
    for _ in range(dimension):
        data.append([random.randint(-10, 10) for _ in range(point_number)])

    return data


def plot_spline2d_test(data):
    spline = compute_spline(*data, 0.1)
    position = spline[:-3]

    # Plot the points
    plt.plot(data[0], data[1], "xb")
    plt.plot(*position, "-r")
    plt.show()


def plot_spline3d_test(data):
    spline = compute_spline(*data, 0.1)
    position = spline[:-3]

    # Plot the points
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(data[0], data[1], data[2], c='b', marker='x')
    ax.scatter(*position, c='r', marker='.')
    plt.show()


if __name__ == '__main__':
    data_2d = generate_data(dimension=2, point_number=10)
    plot_spline2d_test(data_2d)
    data_3d = generate_data(dimension=3, point_number=10)
    plot_spline3d_test(data_3d)
