#! /usr/bin/python
import numpy as np
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

    return *data, s


def test_spline2d():
    import matplotlib.pyplot as plt
    import random

    dimension = 2
    point_number = 10
    data = []
    for _ in range(dimension):
        data.append([random.randint(-10, 10) for _ in range(point_number)])

    rx, ry, o, k, s = compute_spline(*data, 0.1)

    # Plot the points
    plt.plot(data[0], data[1], "xb")
    plt.plot(rx, ry, "-r")
    plt.show()


def test_spline3d():
    import matplotlib.pyplot as plt
    import random

    dimension = 3
    point_number = 10
    data = []
    for _ in range(dimension):
        data.append([random.randint(-10, 10) for _ in range(point_number)])

    rx, ry, rz, o, k, s = compute_spline(*data, 0.1)

    # Plot the points
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(data[0], data[1], data[2], c='b', marker='x')
    ax.scatter(rx, ry, rz, c='r', marker='.')
    plt.show()


if __name__ == '__main__':
    test_spline2d()
    test_spline3d()
