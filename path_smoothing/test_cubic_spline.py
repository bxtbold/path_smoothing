#! /usr/bin/python
import matplotlib.pyplot as plt
import numpy as np

from cubic_spline import CubicSpline
from utils.generate import generate_control_points


def compute_spline(*args):
    position = args[:-1]
    ds = args[-1]

    sp = CubicSpline(*position)
    s = np.arange(0, sp.s[-1], ds)
    # s = np.linspace(0, sp.s[-1] - 1, 100)

    spline = [[] for _ in range(len(position))]

    for i_s in s:
        position = sp.compute_position(i_s)
        for i in range(len(position)):
            spline[i].append(position[i])

    return spline


def plot_spline2d_test(data):
    spline = compute_spline(*data, 1)

    # Plot the points
    plt.plot(data[0], data[1], "xb")
    plt.plot(*spline, "-r")
    plt.show()


def plot_spline3d_test(data):
    spline = compute_spline(*data, 1)

    # Plot the points
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(data[0], data[1], data[2], c='b', marker='x')
    ax.scatter(*spline, c='r', marker='.')
    plt.show()


if __name__ == '__main__':
    control_points_2d = generate_control_points(dimension=2, point_number=10)
    plot_spline2d_test(control_points_2d)
    control_points_3d = generate_control_points(dimension=3, point_number=10, should_x_sequantial=False)
    plot_spline3d_test(control_points_3d)
