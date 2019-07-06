from math import trunc, cos, sin
from operator import truediv


class CurvesDrawer:
    def __init__(self, window, default_window_size, renderer):
        self.__default_window_size = default_window_size
        self.__window = window
        self.__renderer = renderer

    def draw_cissoid(self, a, t_interval, step, color=None):
        def x_parametric(t):
            return a * t ** 2 / (1 + t ** 2)

        def y_parametric(t):
            return a * t ** 3 / (1 + t ** 2)

        self.__draw_parametric(x_parametric, y_parametric, [t_interval], step, color)

    def draw_folium(self, a, t_intervals, step, color=None):
        def x_parametric(t):
            return 3 * a * t / (1 + t ** 3)

        def y_parametric(t):
            return 3 * a * t ** 2 / (1 + t ** 3)

        self.__draw_parametric(x_parametric, y_parametric, t_intervals, step, color)

    def draw_cardioid(self, a, t_interval, step, color=None):
        def x_parametric(t):
            return a * cos(t) * (1 + cos(t))

        def y_parametric(t):
            return a * sin(t) * (1 + cos(t))

        self.__draw_parametric(x_parametric, y_parametric, [t_interval], step, color)

    def draw_snail(self, a, l, t_interval, step, color=None):
        def x_parametric(t):
            return a * cos(t) ** 2 + l * cos(t)

        def y_parametric(t):
            return a * cos(t) * sin(t) + l * sin(t)

        self.__draw_parametric(x_parametric, y_parametric, [t_interval], step, color)

    def draw_epicycloid(self, a, b, t_interval, step, color=None):
        def x_parametric(t):
            return (a + b) * cos(t) - a * cos((a + b) * t / a)

        def y_parametric(t):
            return (a + b) * sin(t) - a * sin((a + b) * t / a)

        self.__draw_parametric(x_parametric, y_parametric, [t_interval], step, color)

    def draw_spiral(self, a, phi_interval, step, color=None):
        def radius(phi):
            return a * (phi ** 3 + 1) ** (3 / 2) / (phi ** 2 + 2)

        def x_parametric(phi):
            return radius(phi) * cos(phi)

        def y_parametric(phi):
            return radius(phi) * sin(phi)

        self.__draw_parametric(x_parametric, y_parametric, [phi_interval], step, color)

    def __draw_parametric(self, x_parametric, y_parametric, t_intervals, step, color=None):
        center_x, center_y = self.__get_window_center(self.__window)
        max_y = self.__window.size[1]
        x_scaling_coeff, y_scaling_coeff = tuple(map(truediv, self.__window.size, self.__default_window_size))

        for t_interval in t_intervals:
            start, end = t_interval
            t = start
            while t < end:
                x = trunc(x_parametric(t) * x_scaling_coeff) + center_x
                y = max_y - (trunc(y_parametric(t) * y_scaling_coeff) + center_y)
                self.__renderer.draw_point((x, y), color)
                t += step
        self.__renderer.present()

    @staticmethod
    def __get_window_center(window):
        return (x // 2 for x in window.size)
