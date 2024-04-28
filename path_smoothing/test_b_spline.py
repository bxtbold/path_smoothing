import matplotlib.pyplot as plt
import random

from b_spline import b_spline_interpolate, b_spline_approximate


def generate_data(dimension, point_number):
    data = []
    for _ in range(dimension):
        data.append([random.randint(-10, 10) for _ in range(point_number)])

    return data


def plot_spline2d_test(control_points):
    b_spline = b_spline_interpolate(*control_points, number_of_points=1000)
    b_spline_app = b_spline_approximate(*control_points, number_of_points=1000)

    # Plot the points
    plt.plot(*b_spline, ".r", label="B-Spline Interploted")
    plt.plot(*b_spline_app, ".g", label="B-Spline Approximate")
    plt.plot(*control_points, "xb", markersize=10, label="Control Points")
    plt.legend()
    plt.show()


def plot_spline3d_test(control_points):
    b_spline = b_spline_interpolate(*control_points, number_of_points=1000)
    b_spline_app = b_spline_approximate(*control_points, number_of_points=1000)

    # Plot the points
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    sizes = [10] * len(b_spline[0])
    ax.scatter(*b_spline, c='r', marker='.', label="B-Spline Interpolated")
    ax.scatter(*b_spline_app, c='g', marker='.', label="B-Spline Approximated")
    ax.scatter(*control_points, sizes, c='b', marker='x', label="Control Points")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    data_2d = generate_data(dimension=2, point_number=10)
    plot_spline2d_test(data_2d)
    data_3d = generate_data(dimension=3, point_number=10)
    plot_spline3d_test(data_3d)
