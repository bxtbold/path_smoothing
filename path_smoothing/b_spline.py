import numpy as np
import scipy.interpolate as scipy_interpolate


class BSpline:

    def __init__(self, x, y, z=None):
        self.x = x
        self.y = y
        if z is not None:
            self.z = z

    def interpolate(self, n_points=100, degree=3):
        n = len(self.x)
        interp_t = np.linspace(0.0, n - 1, n)
        step = np.linspace(0.0, n - 1, n_points)
        interp_points = []

        sx_impl = scipy_interpolate.make_interp_spline(interp_t, self.x, k=degree)
        sy_impl = scipy_interpolate.make_interp_spline(interp_t, self.y, k=degree)
        sx = sx_impl(step)
        sy = sy_impl(step)
        interp_points.append(sx)
        interp_points.append(sy)

        if hasattr(self, "z"):
            sz_impl = scipy_interpolate.make_interp_spline(interp_t, self.z, k=degree)
            sz = sz_impl(step)
            interp_points.append(sz)

        return interp_points

    def interpolate_approximate(self, n_points=100, degree=3):
        n = len(self.x)
        interp_t = np.linspace(0.0, n - 1, n_points)
        interp_points = []

        x_list = list(scipy_interpolate.splrep(range(n), self.x, k=degree))
        y_list = list(scipy_interpolate.splrep(range(n), self.y, k=degree))
        x_list[1] = self.x + [0.0, 0.0, 0.0, 0.0]
        y_list[1] = self.y + [0.0, 0.0, 0.0, 0.0]
        rx = scipy_interpolate.splev(interp_t, x_list)
        ry = scipy_interpolate.splev(interp_t, y_list)

        interp_points.append(rx)
        interp_points.append(ry)

        if hasattr(self, 'z'):
            z_list = list(scipy_interpolate.splrep(range(n), self.z, k=degree))
            z_list[1] = self.z + [0.0, 0.0, 0.0, 0.0]
            rz = scipy_interpolate.splev(interp_t, z_list)
            interp_points.append(rz)

        return interp_points
