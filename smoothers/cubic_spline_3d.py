import numpy as np
import math

from utils import spline

class Spline3D:
    u"""
    3D Cubic Spline class

    """

    def __init__(self, x, y, z):
        self.s = self.__calc_s(x, y, z)
        self.sx = spline.Spline(self.s, x)
        self.sy = spline.Spline(self.s, y)
        self.sz = spline.Spline(self.s, z)

    def __calc_s(self, x, y, z):
        dx = np.diff(x)
        dy = np.diff(y)
        dz = np.diff(z)
        self.ds = [math.sqrt(idx ** 2 + idy ** 2 + idz ** 2)
                   for (idx, idy, idz) in zip(dx, dy, dz)]
        s = [0]
        s.extend(np.cumsum(self.ds))
        return s

    def calc_position(self, s):
        u"""
        calc position
        """
        x = self.sx.calc(s)
        y = self.sy.calc(s)
        z = self.sz.calc(s)

        return x, y, z

    def calc_curvature(self, s):
        u"""
        calc curvature
        """
        dx = self.sx.calcd(s)
        ddx = self.sx.calcdd(s)
        dy = self.sy.calcd(s)
        ddy = self.sy.calcdd(s)
        dz = self.sz.calcd(s)
        ddz = self.sz.calcdd(s)
        k_numerator = (ddy * dx - ddx * dy) * dz - (ddz * dx - ddx * dz) * dy
        k_denominator = (dx ** 2 + dy ** 2 + dz ** 2) ** 1.5
        if k_denominator == 0:
            return 0

        k = k_numerator / k_denominator
        return k

    def calc_orientation(self, s):
        u"""
        calc yaw
        """
        dx = self.sx.calcd(s)
        dy = self.sy.calcd(s)
        dz = self.sz.calcd(s)
        roll = math.atan2(dz, dy)
        pitch = math.atan2(dx, dz)
        yaw = math.atan2(dy, dx)
        return roll, pitch, yaw


def calc_spline_course(x, y, z, ds=0.1):
    sp = Spline3D(x, y, z)
    s = np.arange(0, sp.s[-1], ds)

    rx, ry, rz, ryaw, rk = [], [], [], [], []
    for i_s in s:
        ix, iy, iz = sp.calc_position(i_s)
        rx.append(ix)
        ry.append(iy)
        rz.append(iz)
        ryaw.append(sp.calc_orientation(i_s))
        rk.append(sp.calc_curvature(i_s))

    return rx, ry, rz, ryaw, rk, s


def test_spline3d():
    print("Spline 3D test")
    import matplotlib.pyplot as plt
    import random

    dimension = 3
    point_number = 10
    data = []
    for _ in range(dimension):
        data.append([random.randint(-10, 10) for _ in range(point_number)])

    rx, ry, rz, ryaw, rk, s = calc_spline_course(*data, 0.1)

    # Create a 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot the points
    ax.scatter(rx, ry, rz, c='b', marker='.')

    # Set labels and title
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    ax.set_title('3D Scatter Plot')

    # Show the plot
    plt.show()


if __name__ == '__main__':
    test_spline3d()
