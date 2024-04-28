import numpy as np
import scipy.interpolate as scipy_interpolate


def b_spline_interpolate(x, y, z=None, n_points=100, degree=3):
    n = len(x)
    interp_t = np.linspace(0.0, n - 1, n)
    step = np.linspace(0.0, n - 1, n_points)
    interpolated_points = []

    sx_impl = scipy_interpolate.make_interp_spline(interp_t, x, k=degree)
    sy_impl = scipy_interpolate.make_interp_spline(interp_t, y, k=degree)
    sx = sx_impl(step)
    sy = sy_impl(step)
    interpolated_points.append(sx)
    interpolated_points.append(sy)

    if z is not None:
        sz_impl = scipy_interpolate.make_interp_spline(interp_t, z, k=degree)
        sz = sz_impl(step)
        interpolated_points.append(sz)

    return interpolated_points


def b_spline_approximate(x, y, z=None, n_points=100, degree=3):
    n = len(x)
    interp_t = np.linspace(0.0, n - 1, n_points)
    interpolated_points = []

    x_list = list(scipy_interpolate.splrep(range(n), x, k=degree))
    y_list = list(scipy_interpolate.splrep(range(n), y, k=degree))
    x_list[1] = x + [0.0, 0.0, 0.0, 0.0]
    y_list[1] = y + [0.0, 0.0, 0.0, 0.0]
    rx = scipy_interpolate.splev(interp_t, x_list)
    ry = scipy_interpolate.splev(interp_t, y_list)

    interpolated_points.append(rx)
    interpolated_points.append(ry)

    if z is not None:
        z_list = list(scipy_interpolate.splrep(range(n), z, k=degree))
        z_list[1] = z + [0.0, 0.0, 0.0, 0.0]
        rz = scipy_interpolate.splev(interp_t, z_list)
        interpolated_points.append(rz)

    return interpolated_points
