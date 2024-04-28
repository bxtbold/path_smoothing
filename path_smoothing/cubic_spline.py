import math
import numpy as np
from utils.spline import Spline


class CubicSpline:
    def __init__(self, x, y, z=None):
        self.s = self.__compute_s(x, y, z)
        self.sx = Spline(self.s, x)
        self.sy = Spline(self.s, y)
        if z:
            self.sz = Spline(self.s, z)

    def __compute_s(self, x, y, z=None):
        dx = np.diff(x)
        dy = np.diff(y)
        if z:
            dz = np.diff(z)
            self.ds = [math.sqrt(idx ** 2 + idy ** 2 + idz ** 2)
                    for (idx, idy, idz) in zip(dx, dy, dz)]
        else:
            self.ds = [math.sqrt(idx ** 2 + idy ** 2)
                    for (idx, idy) in zip(dx, dy)]
        s = [0]
        s.extend(np.cumsum(self.ds))
        return s

    def compute_position(self, s):
        x = self.sx.compute_position(s)
        y = self.sy.compute_position(s)
        if hasattr(self, 'sz'):
            z = self.sz.compute_position(s)
            return x, y, z
        return x, y

    def compute_curvature(self, s):
        dx = self.sx.get_dt(s)
        ddx = self.sx.get_ddt(s)
        dy = self.sy.get_dt(s)
        ddy = self.sy.get_ddt(s)
        if hasattr(self, 'sz'):
            dz = self.sz.get_dt(s)
            ddz = self.sz.get_ddt(s)
            k_numerator = (ddy * dx - ddx * dy) * dz - (ddz * dx - ddx * dz) * dy
            k_denominator = (dx ** 2 + dy ** 2 + dz ** 2) ** 1.5
        else:
            k_numerator = ddy * dx - ddx * dy
            k_denominator = (dx ** 2 + dy ** 2) ** 1.5
        if k_denominator == 0:
            return 0
        k = k_numerator / k_denominator
        return k

    def compute_orientation(self, s):
        dx = self.sx.get_dt(s)
        dy = self.sy.get_dt(s)
        if hasattr(self, 'sz'):
            dz = self.sz.get_dt(s)
            roll = math.atan2(dz, dy)
            pitch = math.atan2(dx, dz)
            yaw = math.atan2(dy, dx)
            return roll, pitch, yaw
        else:
            yaw = math.atan2(dy, dx)
            return 0, 0, yaw

    def compute_yaw(self, s):
        dx = self.sx.get_dt(s)
        dy = self.sy.get_dt(s)
        yaw = math.atan2(dy, dx)
        return yaw

    def compute_roll(self, s):
        if hasattr(self, 'sz'):
            dy = self.sy.get_dt(s)
            dz = self.sz.get_dt(s)
            roll = math.atan2(dz, dy)
            return roll
        return 0

    def compute_pitch(self, s):
        if hasattr(self, 'sz'):
            dx = self.sx.get_dt(s)
            dz = self.sz.get_dt(s)
            pitch = math.atan2(dx, dz)
            return pitch
        return 0
