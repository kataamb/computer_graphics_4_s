"""
    Модуль для вывода сообщений
"""

import tkinter as tk
from PIL import ImageTk, Image


NAME = 'Амбарцумова Екатерина'
GROUP = 'ИУ7-45Б'
AUTHOR = NAME + '\n' + GROUP

IMAGE_PATH = 'images/'
MSGS_PATH = IMAGE_PATH + 'msg_icons/'
INFO_ICON = MSGS_PATH + 'info_icon.png'
ERROR_ICON = MSGS_PATH + 'error_icon.png'

"""
PROBLEM_TEXT = ('На  плоскости  дано  множество точек. Найти такой\n'
                + 'треугольник с вершинами в этих точках, у которого\n'
                + 'разность  максимального и минимального количества\n'
                + 'точек,  попавших  в каждый из 6-ти треугольников,\n'
                + 'образованных  пересечением  медиан,  максимальна.\n'
                + 'Сделать  в  графическом  режиме  вывод полученной\n'
                + 'картинки.')

"""
levels = []


def create_okbox(title, text, image_path, shift):
    """
        Создание сообщения с одной кнопкой OK
    """
    infobox = tk.Toplevel()
    levels.append(infobox)
    infobox.title(title)
    infobox.geometry(shift)
    infobox.resizable(False, False)

    pil_img = Image.open(image_path).resize((60, 60))
    img = ImageTk.PhotoImage(pil_img)

    lbl_img = tk.Label(infobox)
    lbl_img.grid(row=1, column=1)
    lbl_img.image = img
    lbl_img.configure(image=img)

    lbl_text = tk.Label(infobox)
    lbl_text.grid(row=1, column=3)
    lbl_text.configure(text=text, justify=tk.LEFT, font=('Courier', 12))

    btn_ok = tk.Button(infobox)
    btn_ok.grid(row=3, column=0, columnspan=5)
    btn_ok.configure(text='OK')
    btn_ok.configure(command=infobox.destroy)


def create_infobox(title, text):
    """
        Создание информационного сообщения
    """
    create_okbox(title, text, INFO_ICON, '+700+450')


def create_errorbox(title, text):
    """
        Создание сообщения об ошибке
    """
    create_okbox(title, text, ERROR_ICON, '+700+450')


def create_hintbox(title, text):
    """
        Создание сообщения с подсказкой
    """
    create_okbox(title, text, INFO_ICON, '+1300+200')


def author():
    """
        Вывод сообщения об авторе
    """
    create_infobox('Об авторе', AUTHOR)

def destroy_toplevels():
    """
        Закрытие всех окон сообщений
    """
    for level in levels:
        level.destroy()
