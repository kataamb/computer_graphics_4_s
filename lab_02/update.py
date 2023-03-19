"""
    Модуль для обновления изображения
"""

import tkinter as tk
import copy

import messages as msg


NONNUMERIC = 'Нечисловые данные'
EMPTY = 'Пустой ввод'

NONNUM_MOVE = 'dx и dy должны быть представлены вещественными числами'
EMPTY_MOVE = 'Для выполнения переноса заполните поля dx и dy'

NONNUM_SCALE = 'Xc, Yc, Kx и Ky должны быть представлены вещественными числами'
EMPTY_SCALE = 'Для выполнения масштабирования заполните поля Xc, Yc, Kx и Ky'

NONNUM_ROTATION = 'Xc, Yc и угол должны быть представлены вещественными числами'
EMPTY_ROTATION = 'Для выполнения поворота заполните поля Xc, Yc и "Угол (°)"'

FONT = 'DejaVu Sans Mono'
FONT_SIZE = 14
FONT_CONFIG = (FONT, FONT_SIZE)


class History:
    """
        Класс истории состояний изображения
    """
    def __init__(self, index, buf):
        """
            Коструктор класса
        """
        self.index = index
        self.buf = buf


    def add(self, func):
        """
            Добавление состояния в историю
        """
        self.index += 1
        self.buf = self.buf[:self.index] + [func]


    def back(self, fish):
        """
            Шаг назад
        """
        self.index -= 1
        self.update_fish(fish)


    def forward(self, fish):
        """
            Шаг вперед
        """
        self.index += 1
        self.update_fish(fish)


    def update_tank(self, tank):
        """
            Постановка текущего состояния
        """
        tank_copy = copy.deepcopy(self.buf[self.index])

        for i, part in enumerate(tank_copy.full):
            tank.full[i] = part


def renew_label(window):
    """
        Обновление показанных координат
        центра фигуры
    """
    window.lbl_figure_centre.configure(
        font=FONT_CONFIG,
        text="X:{:7.2f}; Y:{:7.2f}".format(window.funcs[0].x_list[0],
                                           window.funcs[0].y_list[0])
        )


def move(window, tank, tanks):
    """
        Запуск переноса
    """
    try:
        dx = float(window.ent_dx.get())
        dy = float(window.ent_dy.get())

    except ValueError:
        if window.ent_dx.get() and window.ent_dy.get():
            msg.create_errorbox(NONNUMERIC, NONNUM_MOVE)
        else:
            msg.create_errorbox(EMPTY, EMPTY_MOVE)

    else:
        tank.move(dx, dy)
        tanks.add(copy.deepcopy(tank))
        window.funcs = tank.full
        window.btn_undo.configure(state=tk.NORMAL)
        window.btn_redo.configure(state=tk.DISABLED)
        window.create_matplotlib()
        renew_label(window)


def scale(window, tank, tanks):
    """
        Запуск масштабирования
    """
    try:
        kx = float(window.ent_kx.get())
        ky = float(window.ent_ky.get())
        xc = float(window.ent_xc.get())
        yc = float(window.ent_yc.get())

    except ValueError:
        if (window.ent_kx.get() and window.ent_ky.get()
                and window.ent_xc.get() and window.ent_yc.get()):
            msg.create_errorbox(NONNUMERIC, NONNUM_SCALE)
        else:
            msg.create_errorbox(EMPTY, EMPTY_SCALE)

    else:
        tank.scaling(kx, ky, xc, yc)
        tanks.add(copy.deepcopy(tank))
        window.funcs = tank.full
        window.btn_undo.configure(state=tk.NORMAL)
        window.btn_redo.configure(state=tk.DISABLED)
        window.create_matplotlib()
        renew_label(window)


def rotate(window, tank, tanks):
    """
        Запуск масштабирования
    """
    try:
        phi = float(window.ent_angle.get())
        xc = float(window.ent_xc.get())
        yc = float(window.ent_yc.get())

    except ValueError:
        if (window.ent_xc.get() and window.ent_yc.get()
                and window.ent_angle.get()):
            msg.create_errorbox(NONNUMERIC, NONNUM_ROTATION)
        else:
            msg.create_errorbox(EMPTY, EMPTY_ROTATION)

    else:
        tank.rotate(phi, xc, yc)
        tanks.add(copy.deepcopy(tank))
        window.btn_undo.configure(state=tk.NORMAL)
        window.btn_redo.configure(state=tk.DISABLED)
        window.funcs = tank.full
        window.create_matplotlib()
        renew_label(window)


def reset(window, tank, tanks):
    """
        Возвращение к исходному изображению
        с сохранением предыдущего состояния
    """
    tank.reset()
    window.funcs = tank.full
    window.create_matplotlib()
    tanks.add(copy.deepcopy(tank))
    window.btn_undo.configure(state=tk.NORMAL)
    window.btn_redo.configure(state=tk.DISABLED)
    renew_label(window)


def undo(window, tank, tanks):
    """
        Возвращение к предыдущему состоянию изображения
    """
    if tanks.index:
        tanks.back(tank)
        window.funcs = tank.full
        window.create_matplotlib()
        window.btn_redo.configure(state=tk.NORMAL)
        renew_label(window)

    if not tanks.index:
        window.btn_undo.configure(state=tk.DISABLED)


def redo(window, tank, tanks):
    """
        Возвращение к предыдущему состоянию изображения
    """
    if tanks.index < len(tanks.buf):
        tanks.forward(tank)
        tank = tanks.buf[tanks.index]
        window.funcs = tank.full
        window.create_matplotlib()
        window.btn_undo.configure(state=tk.NORMAL)
        renew_label(window)

    if tanks.index == len(tanks.buf) - 1:
        window.btn_redo.configure(state=tk.DISABLED)
