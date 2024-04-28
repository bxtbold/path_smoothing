import matplotlib.pyplot as plt

from b_spline import BSpline
from utils.generate import generate_control_points


def plot_spline2d_test(control_points):
    b_spline = BSpline(*control_points)
    b_spline_interp = b_spline.interpolate(n_points=100, degree=3)
    b_spline_approx = b_spline.interpolate_approximate(n_points=100, degree=3)

    # Plot the points
    plt.plot(*b_spline_interp, ".r", label="B-Spline Interploted")
    plt.plot(*b_spline_approx, ".g", label="B-Spline Approximate")
    plt.plot(*control_points, "xb", markersize=10, label="Control Points")
    plt.legend()
    plt.show()


def plot_spline3d_test(control_points):
    b_spline = BSpline(*control_points)
    b_spline_interp = b_spline.interpolate(n_points=100, degree=3)
    b_spline_approx = b_spline.interpolate_approximate(n_points=100, degree=3)

    # Plot the points
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(*b_spline_interp, c='r', marker='.', label="B-Spline Interpolated")
    ax.scatter(*b_spline_approx, c='g', marker='.', label="B-Spline Approximated")
    ax.scatter(*control_points, c='b', marker='x', label="Control Points")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    control_points_2d = generate_control_points(dimension=2, point_number=10)
    plot_spline2d_test(control_points_2d)
    control_points_3d = generate_control_points(dimension=3, point_number=10)
    plot_spline3d_test(control_points_3d)
