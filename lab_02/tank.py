"""
    Модуль для работы с изображением рыбы
"""

from math import sin, cos
import numpy as np

class Func:
    """
        Класс функции, заданной узлами
    """
    def __init__(self, x_list, y_list):
        self.x_list = x_list
        self.y_list = y_list


class Tank:
    """
        Класс изображения танка
    """
    def __init__(self):
        """
            Конструктор класса
        """

        self.cabin_up = self.create_cabin_up()
        self.caterpillar_down = self.create_caterpillar_down()
        self.center = self.create_center()
        self.full = [self.center, self.cabin_up, self.caterpillar_down]
        self.wheels = self.create_wheels()


    def reset(self):
        """
            Сброс
        """
        self.__init__()

    def create_center(self):
        center = Func([], [])
        center.x_list = [0]
        center.y_list = [0]
        return center


    def create_body(self, large_sa, small_sa):
        """
            Создание эллипса (колесо)
        """
        body = Func([], [])
        angles = np.linspace(0, 360, 360)

        for angle in angles:
            body.x_list.append(large_sa * cos(np.radians(angle)))
            body.y_list.append(small_sa * sin(np.radians(angle)))

        return body


    def create_head(self):
        """
            Создание колеса
        """
        head = self.create_body(5, 5)
        head.x_list = [x - 17 for x in head.x_list]

        return head


    def create_wheel(self, x_c, y_c, rad):
        """
            Создание колеса
        """
        eye = self.create_body(rad, rad)
        eye.x_list = [x + x_c for x in eye.x_list]
        eye.y_list = [y + y_c for y in eye.y_list]

        return eye

    def create_wheels(self):
        centers = [  [-1.3*8, -3*8, 4], [0, -3*8, 4],  [1.5*8, -3*8, 4], [3*8, -3*8, 4], [3*8, -3*8, 4], [4.5*8, -2.6*8, 4]]
        wheels = []
        for c in centers:
            wheel = self.create_wheel(c[0], c[1], c[2])
            inner_wheel = self.create_wheel(c[0], c[1], c[2] / 2)
            wheels.append(wheel)
            wheels.append(inner_wheel)
        self.full += wheels

        return wheels







    def create_cabin_up(self):
        cabin_up = Func([], [])
        x = [-8, -13.6, -24, -52.0, -52.0, -24, -12.0, -4.0, 8, 9.6, 24, 24, 12.0, 12.0, 32, 44.0, 36.0, -24, -22.4, -8]
        y = [0, 8, 8, 10.4, 12.0, 13.6, 13.6, 20.0, 20.0, 16, 8, 0, 0, -1.6, -1.6, -12.0, -16, -16, -9.6, 0]
        cabin_up.x_list = x
        cabin_up.y_list = y
        return cabin_up

    def create_caterpillar_down(self):
        caterpillar = Func([], [])

        x = [44,  40, 24, -12.0, -24]
        y = [-12,  -24, -28.0, -28.0, -16]
        caterpillar.x_list = x
        caterpillar.y_list = y
        return caterpillar



    def move(self, dx, dy):
        """
            Перенос изображения
        """
        for element in self.full:
            element.x_list = [x + dx for x in element.x_list]
            element.y_list = [y + dy for y in element.y_list]


    def scaling(self, kx, ky, xc, yc):
        """
            Масштабирование изображения
        """
        for element in self.full:
            element.x_list = [x * kx + (1 - kx) * xc for x in element.x_list]
            element.y_list = [y * ky + (1 - ky) * yc for y in element.y_list]


    def rotate(self, phi, xc, yc):
        """
            Поворот изображения
        """
        phi = -phi
        for element in self.full:
            tmp_x = [x for x in element.x_list]
            element.x_list = [xc + (x - xc) * cos(np.radians(phi))
                              + (element.y_list[i] - yc) * sin(np.radians(phi))
                              for i, x in enumerate(element.x_list)]
            element.y_list = [yc - (tmp_x[i] - xc) * sin(np.radians(phi))
                              + (y - yc) * cos(np.radians(phi))
                              for i, y in enumerate(element.y_list)]
