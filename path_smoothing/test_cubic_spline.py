#! /usr/bin/python
import matplotlib.pyplot as plt

from cubic_spline import CubicSpline
from utils.generate import generate_control_points


def plot_spline2d_test(control_points):
    spline = CubicSpline(*control_points)
    interp_points = spline.interpolate(0.1)

    # Plot the points
    plt.plot(*interp_points, "-r")
    plt.plot(*control_points, "xb")
    plt.show()


def plot_spline3d_test(control_points):
    spline = CubicSpline(*control_points)
    interp_points = spline.interpolate(0.1)

    # Plot the points
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(*interp_points, c='r', marker='.')
    ax.scatter(*control_points, c='b', marker='x')
    plt.show()


if __name__ == '__main__':
    control_points_2d = generate_control_points(dimension=2, point_number=10)
    plot_spline2d_test(control_points_2d)
    control_points_3d = generate_control_points(dimension=3, point_number=10)
    plot_spline3d_test(control_points_3d)
