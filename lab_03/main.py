import numpy as np
import tkinter as tk
import matplotlib.pyplot as plt
from tkinter import colorchooser, messagebox

from dda import DDA
from brezenhem import *
from vu import VU
from draw import *
from config import *

root = tk.Tk()
root.title("ЛР3")
root["bg"] = MAIN_COLOUR

root.geometry(str(WINDOW_WIDTH) + "x" + str(WINDOW_HEIGHT))

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CANVAS FILED FOR DRAWING lines and spectres by algorithms
canvasFiled = tk.Canvas(root, bg=CANVAS_COLOUR)
canvasFiled.pack(fill='both', expand=True, side='right')
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------



# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
def clearScreen():
    canvasFiled.delete("all")
    drawAxes()


def drawAxes():
    color = 'gray'
    canvasFiled.create_line(0, 3, CANVAS_WIDTH, 3, width=1, fill='light gray', arrow=tk.LAST)
    canvasFiled.create_line(3, 0, 3, CANVAS_HEIGHT, width=1, fill='light gray', arrow=tk.LAST)
    for i in range(50, int(CANVAS_WIDTH), 50):
        canvasFiled.create_text(i, 15, text=str(abs(i)), fill=color)
        canvasFiled.create_line(i, 0, i, 5, fill=color)

    for i in range(50, int(CANVAS_HEIGHT), 50):
        canvasFiled.create_text(20, i, text=str(abs(i)), fill=color)
        canvasFiled.create_line(0, i, 5, i, fill=color)


def drawLine():

    algorithm = algorithmsRB.get()
    xStart = xsEntry.get()
    yStart = ysEntry.get()
    xEnd = xeEntry.get()
    yEnd = yeEntry.get()

    if not xStart or not yStart:
        messagebox.showwarning('Ошибка ввода',
                               'Не заданы координаты начала отрезка!')
    elif not xEnd or not yEnd:
        messagebox.showwarning('Ошибка ввода',
                               'Не заданы координаты конца отрезка!')
    else:
        try:
            xStart, yStart = float(xStart), float(yStart)
            xEnd, yEnd = float(xEnd), float(yEnd)
        except all:
            messagebox.showwarning('Ошибка ввода',
                                   'Координаты заданы неверно!')
        if algorithm == 0:
            drawLineBy_algorithm(canvasFiled, DDA(xStart, yStart, xEnd, yEnd, colour=LINE_COLOUR))
        elif algorithm == 1:
            drawLineBy_algorithm(canvasFiled, BrezenhemFloat(xStart, yStart, xEnd, yEnd, colour=LINE_COLOUR))
        elif algorithm == 2:
            drawLineBy_algorithm(canvasFiled, BrezenhemInteger(xStart, yStart, xEnd, yEnd, colour=LINE_COLOUR))
        elif algorithm == 3:
            drawLineBy_algorithm(canvasFiled, BrezenhemSmooth(canvasFiled, xStart, yStart, xEnd, yEnd, LINE_COLOUR))
        elif algorithm == 4:
            drawLineBy_algorithm(canvasFiled, VU(canvasFiled, xStart, yStart, xEnd, yEnd, fill=LINE_COLOUR))
        elif algorithm == 5:
            drawLineBy_StandartAlgorithm(canvasFiled, xStart, yStart, xEnd, yEnd, colour=LINE_COLOUR)


def drawSpecter():
    algorithm = algorithmsRB.get()
    xStart = xsEntry.get()
    yStart = ysEntry.get()
    xEnd = xeEntry.get()
    yEnd = yeEntry.get()
    angle = angleEntry.get()

    if not xStart or not yStart:
        messagebox.showwarning('Ошибка ввода',
                               'Не заданы координаты начала отрезка!')
    elif not xEnd or not yEnd:
        messagebox.showwarning('Ошибка ввода',
                               'Не заданы координаты конца отрезка!')
    else:
        try:
            xStart, yStart = float(xStart), float(yStart)
            xEnd, yEnd = float(xEnd), float(yEnd)
            angle = float(angle)
        except all:
            messagebox.showwarning('Ошибка ввода',
                                   'Координаты заданы неверно!')

        if algorithm == 0:
            drawSpecterBy_Method(canvasFiled, DDA,
                                 xStart, yStart,
                                 xEnd, yEnd, angle,
                                 LINE_COLOUR)
        elif algorithm == 1:
            drawSpecterBy_Method(canvasFiled, BrezenhemFloat,
                                 xStart, yStart,
                                 xEnd, yEnd, angle,
                                 LINE_COLOUR)
        elif algorithm == 2:
            drawSpecterBy_Method(canvasFiled, BrezenhemInteger,
                                 xStart, yStart,
                                 xEnd, yEnd, angle,
                                 LINE_COLOUR)
        elif algorithm == 3:
            drawSpecterBy_Method(canvasFiled, BrezenhemSmooth,
                                 xStart, yStart,
                                 xEnd, yEnd, angle,
                                 LINE_COLOUR, intensive=True)
        elif algorithm == 4:
            drawSpecterBy_Method(canvasFiled, VU,
                                 xStart, yStart,
                                 xEnd, yEnd, angle,
                                 LINE_COLOUR, intensive=True)
        elif algorithm == 5:
            drawSpecterBy_StardartMethod(canvasFiled, xStart, yStart, xEnd, yEnd, angle, LINE_COLOUR)


def timeInput(mode):
    try:
        length = int(lengthEntry.get())

        if length <= 0:
            messagebox.showwarning('Ошибка ввода',
                                       'Длина для измерений должна быть больше нуля!')
        else:
            if mode == 1:
                time_bar(length)
            else:
                step_bar(length)
    except all:
        messagebox.showwarning('Ошибка ввода',
                               'Длина для измерений задана неверно!')


def close_plt():
    plt.figure("Исследование времени работы алгоритмов построения.",)
    plt.close()
    plt.figure("Исследование ступенчатости алгоритмов построение.")
    plt.close()


# гистограмма времени
def time_bar(length):
    close_plt()

    plt.figure("Исследование времени работы алгоритмов построения.", figsize=(9, 7))
    times = list()
    angle = 1
    pb = [375, 200]
    pe = [pb[0] + length, pb[0]]

    times.append(drawSpecterBy_Method(canvasFiled, DDA, pb[0], pb[1], pe[0], pe[1], angle, CANVAS_COLOUR, draw=False))
    times.append(drawSpecterBy_Method(canvasFiled, BrezenhemFloat, pb[0], pb[1], pe[0], pe[1], angle, CANVAS_COLOUR, draw=False))
    times.append(drawSpecterBy_Method(canvasFiled, BrezenhemInteger, pb[0], pb[1], pe[0], pe[1], angle, CANVAS_COLOUR, draw=False))
    times.append(drawSpecterBy_Method(canvasFiled, BrezenhemSmooth, pb[0], pb[1], pe[0], pe[1], angle, CANVAS_COLOUR, draw=False, intensive=True))
    times.append(drawSpecterBy_Method(canvasFiled, VU, pb[0], pb[1], pe[0], pe[1], angle, CANVAS_COLOUR, draw=False, intensive=True))
    for i in range(len(times)):
        times[i] *= 100

    Y = range(len(times))

    L = ('ЦДА', 'Брезенхем с\nдействительными\nкоэффицентами',
         'Брезенхем с\nцелыми\nкоэффицентами', 'Брезенхем с\nс устранением\nступенчатости', 'Ву')
    plt.bar(Y, times, align='center')
    plt.xticks(Y, L)
    plt.ylabel("Cекунды (длина линии " + str(length) + ")")
    plt.show()


def step_bar(length):
    close_plt()

    angle = 0
    step = 2
    pb = [0, 0]
    pe = [pb[0], pb[1] + length]

    angles = []
    DDA_steps = []
    BrezenhemInteger_steps = []
    BrezenhemFloat_steps = []
    BrezenhemSmooth_steps = []
    VU_steps = []

    for j in range(90 // step):
        DDA_steps.append(DDA(pb[0], pb[1], pe[0], pe[1], stepmode=True))
        BrezenhemInteger_steps.append(BrezenhemInteger(pb[0], pb[1], pe[0], pe[1], stepmode=True))
        BrezenhemFloat_steps.append(BrezenhemFloat(pb[0], pb[1], pe[0], pe[1], stepmode=True))
        BrezenhemSmooth_steps.append(BrezenhemSmooth(canvasFiled, pb[0], pb[1], pe[0], pe[1], stepmode=True))
        VU_steps.append(VU(canvasFiled, pb[0], pb[1], pe[0], pe[1], stepmode=True))

        pe[0], pe[1] = turn_point(radians(step), pe[0], pe[1], pb[0], pb[1])
        angles.append(angle)
        angle += step

    plt.figure("Исследование ступенчатости алгоритмов построение.", figsize=(18, 10))

    plt.subplot(2, 3, 1)
    plt.plot(angles, DDA_steps, label="ЦДА")
    plt.plot(angles, BrezenhemInteger_steps, '--', label="Брензенхем с целыми или\nдействительными коэффицентами")
    plt.plot(angles, BrezenhemInteger_steps, '.', label="Брензенхем с устр\nступенчатости")
    plt.plot(angles, VU_steps, '-.', label="By")
    plt.title("Исследование ступенчатости.\n{0} - длина отрезка".format(length))
    plt.xticks(np.arange(91, step=5))
    plt.legend()
    plt.ylabel("Количество ступенек")
    plt.xlabel("Угол в градусах")

    plt.subplot(2, 3, 2)
    plt.title("ЦДА")
    plt.plot(angles, DDA_steps)
    plt.xticks(np.arange(91, step=5))
    plt.ylabel("Количество ступенек")
    plt.xlabel("Угол в градусах")

    plt.subplot(2, 3, 3)
    plt.title("BУ")
    plt.plot(angles, VU_steps)
    plt.xticks(np.arange(91, step=5))
    plt.ylabel("Количество ступенек")
    plt.xlabel("Угол в градусах")

    plt.subplot(2, 3, 4)
    plt.title("Брензенхем с действительными коэффицентами")
    plt.plot(angles, BrezenhemFloat_steps)
    plt.xticks(np.arange(91, step=5))
    plt.ylabel("Количество ступенек")
    plt.xlabel("Угол в градусах")

    plt.subplot(2, 3, 5)
    plt.title("Брензенхем с целыми коэффицентами")
    plt.plot(angles, BrezenhemInteger_steps)
    plt.xticks(np.arange(91, step=5))
    plt.ylabel("Количество ступенек")
    plt.xlabel("Угол в градусах")

    plt.subplot(2, 3, 6)
    plt.title("Брензенхем с устр. ступенчатости")
    plt.plot(angles, BrezenhemSmooth_steps)
    plt.xticks(np.arange(91, step=5))
    plt.ylabel("Количество ступенек")
    plt.xlabel("Угол в градусах")

    plt.show()

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Фрейм для ввода данных


dataFrame = tk.Frame(root)
dataFrame["bg"] = MAIN_FRAME_COLOR

dataFrame.pack(fill='both', expand=True, side='right')
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Кнопки для выбора алгоритма

algorithmsFrame = tk.Frame(dataFrame)
algorithmsFrame.pack(fill='both', expand=True, side='top')

algorithmsLabel = tk.Label(algorithmsFrame, bg=MAIN_COLOUR_LABEL_BG, text="АЛГОРИТМЫ ПОСТРОЕНИЯ",
                     font=("Consolas", 16),
                     fg=MAIN_COLOUR_LABEL_TEXT, relief=tk.SOLID)

algorithmsArr = [("Цифровой дифференциальный анализатор", 0),
                 ("Брензенхем (float)", 1),
                 ("Брензенхем (integer)", 2),
                 ("Брензенхем (c устр. ступенчатости)", 3),
                 ("By", 4),
                 ("Библиотечная функция", 5)]
algorithmsRB = tk.IntVar()

for value in range(len(algorithmsArr)):
    tk.Radiobutton(algorithmsFrame, variable=algorithmsRB, text=algorithmsArr[value][0], value=value, bg="lightblue",
                   indicatoron=False, font=("Consolas", 16), justify=tk.LEFT, highlightbackground="black",
                   ).pack(fill='both', expand=True, side='bottom')

algorithmsLabel.pack(fill='both', expand=True, side='bottom')
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

ColorSettings = tk.Frame(dataFrame)
ColorSettings.pack(fill='both', expand=True, side='top')

# ВЫБОР цвета
chooseColourMainLabel = tk.Label(ColorSettings, bg=MAIN_COLOUR_LABEL_BG, text="ВЫБОР ЦВЕТА",
                     font=("Consolas", 16),
                     fg=MAIN_COLOUR_LABEL_TEXT, relief=tk.SOLID)

size = (DATA_FRAME_WIGHT // 1.5) // 8

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Выбор цвета фона

def get_color_bg():
    color_code = colorchooser.askcolor(title="Choose colour background canvas")
    set_bgcolour(color_code[-1])


def set_bgcolour(color):
    global CANVAS_COLOUR
    CANVAS_COLOUR = color
    canvasFiled.configure(bg=CANVAS_COLOUR)


bgColourBtn = tk.Button(ColorSettings, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT,
                        text='Выбрать цвет фона', font=("Consolas", 14), command=get_color_bg)
chooseColourMainLabel.pack(fill='both', expand=True, side='top')
bgColourBtn.pack(fill='both', expand=True, side='top')

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# выбор цвета линии



lineCurColourTextLabel = tk.Label(ColorSettings, bg=MAIN_FRAME_COLOR, text="Текущий цвет линии:",
                     font=("Consolas", 16),
                     fg=MAIN_COLOUR_LABEL_TEXT)

lineCurColourLabel = tk.Label(dataFrame, bg="black")


def get_colour_line():
    color_code = colorchooser.askcolor(title="Choose colour line")
    set_linecolour(color_code[-1])


def set_linecolour(color):
    global LINE_COLOUR
    LINE_COLOUR = color
    lineCurColourLabel.configure(bg=LINE_COLOUR)


lineColourBtn = tk.Button(ColorSettings, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text='Выбрать другой цвет линии', font=("Consolas", 14), command=get_colour_line)

lineColourBtn.pack(fill='both', expand=True, side='top')
lineCurColourTextLabel.pack(fill='both', expand=True, side='top')
lineCurColourLabel.pack(fill='both', expand=True, side='top')

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Построение линии
LineMakeFrame = tk.Frame(dataFrame)
LineMakeFrame.pack(fill='both', expand=True, side='top')


lineMakeLabel = tk.Label(LineMakeFrame, bg=MAIN_COLOUR_LABEL_BG, text="ПОСТРОЕНИЕ ЛИНИИ",
                     font=("Consolas", 16),
                     fg=MAIN_COLOUR_LABEL_TEXT, relief=tk.SOLID)

lineMakeLabel.pack(fill='both', expand=True, side='top')


CoordinatesLabelFrame = tk.Frame(LineMakeFrame)
CoordinatesLabelFrame.pack(fill='both', expand=True, side='top')

#argumnetsLabel = tk.Label(CoordinatesLabelFrame, bg=MAIN_FRAME_COLOR, text="Xн         Yн         Xк          Yк",
#                     font=("Consolas", 14),
#                     fg=MAIN_COLOUR_LABEL_TEXT)

# label'ы для координат
labels_names = ['Xн',  'Yн', 'Xк', 'Yк']
for name in labels_names:
    label_name = tk.Label(CoordinatesLabelFrame, bg=MAIN_FRAME_COLOR, text=name,
                          font=("Consolas", 14),
                     fg=MAIN_COLOUR_LABEL_TEXT)
    label_name.pack(fill='both', expand=True, side='left')


CoordinatesInputFrame = tk.Frame(LineMakeFrame)
CoordinatesInputFrame.pack(fill='both', expand=True, side='top')

xsEntry = tk.Entry(CoordinatesInputFrame, bg=MAIN_COLOUR_LABEL_TEXT, font=("Consolas", 14), fg=MAIN_FRAME_COLOR, justify="center")
ysEntry = tk.Entry(CoordinatesInputFrame, bg=MAIN_COLOUR_LABEL_TEXT, font=("Consolas", 14), fg=MAIN_FRAME_COLOR, justify="center")
xeEntry = tk.Entry(CoordinatesInputFrame, bg=MAIN_COLOUR_LABEL_TEXT, font=("Consolas", 14), fg=MAIN_FRAME_COLOR, justify="center")
yeEntry = tk.Entry(CoordinatesInputFrame, bg=MAIN_COLOUR_LABEL_TEXT, font=("Consolas", 14), fg=MAIN_FRAME_COLOR, justify="center")
drawLineBtn = tk.Button(LineMakeFrame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text="Построить линию", font=("Consolas", 14),
                        command=drawLine)


xsEntry.pack(fill='both', expand=True, side='left')
ysEntry.pack(fill='both', expand=True, side='left')
xeEntry.pack(fill='both', expand=True, side='left')
yeEntry.pack(fill='both', expand=True, side='left')
drawLineBtn.pack(fill='both', expand=True, side='left')
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Построение спектра

spectrumMakeLabel = tk.Label(dataFrame, bg=MAIN_COLOUR_LABEL_BG, text="ПОСТРОЕНИЕ СПЕКТРА",
                     font=("Consolas", 16),
                     fg=MAIN_COLOUR_LABEL_TEXT, relief=tk.SOLID)

spectrumMakeLabel.pack(fill='both', expand=True, side='top')

lineColourLabel = tk.Label(dataFrame, bg=MAIN_FRAME_COLOR, text="Угол поворота (в градуссах):",
                     font=12,
                     fg=MAIN_COLOUR_LABEL_TEXT)
angleEntry = tk.Entry(dataFrame, bg=MAIN_COLOUR_LABEL_TEXT, font=("Consolas", 14), fg=MAIN_FRAME_COLOR, justify="center")
drawSpnBtn = tk.Button(dataFrame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text="Построить спектр", font=("Consolas", 14),
                       command=drawSpecter)

lineColourLabel.pack(fill='both', expand=True, side='top')
angleEntry.pack(fill='both', expand=True, side='top')
drawSpnBtn.pack(fill='both', expand=True, side='top')
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Кнопки сравнения, очистки и справки

otherOptions = tk.Label(dataFrame, bg=MAIN_COLOUR_LABEL_BG, text="ДОПОЛНИТЕЛЬНО",
                     font=("Consolas", 16),
                     fg=MAIN_COLOUR_LABEL_TEXT, relief=tk.SOLID)

otherOptions.pack(fill='both', expand=True, side='top')


def show_info():
    messagebox.showinfo('Информация',
                        'С помощью данной программы можно построить отрезки 6 способами:\n'
                        '1) методом цифрового дифференциального анализатора;\n'
                        '2) методом Брезенхема с действитльными коэфициентами;\n'
                        '3) методом Брезенхема с целыми коэфициентами;\n'
                        '4) методом Брезенхема с устранением ступенчатости;\n'
                        '5) методом Ву;\n'
                        '6) стандартым методом.\n'
                        '\nДля построения отрезка необходимо задать его начало\n'
                        'и конец и выбрать метод построения из списка предложенных.\n'
                        '\nДля построения спектра (пучка отрезков)\n'
                        'необходимо задать начало и конец,\n'
                        'выбрать метод для построения,\n'
                        'а также угол поворота отрезка.\n'
                        '\nДля анализа ступенчатости достаточно нажать на кнопку "Сравнение ступенчатости".\n'
                        'Анализ ступенчатости и времени исполнения приводится\n'
                        'в виде графиков pyplot.\n'
                        'Введите длину отрезка, если хотите сделать анализ программы\n'
                        'при построении отрезков определенной длины.\n\n'
                        'Автор: Амбарцумова Екатерина\n'
                        'ИУ7-45Б')


lineLengthLabel = tk.Label(dataFrame, bg=MAIN_FRAME_COLOR, text="Длина линии:",
                     font=12,
                     fg=MAIN_COLOUR_LABEL_TEXT)
lengthEntry = tk.Entry(dataFrame, bg=MAIN_COLOUR_LABEL_TEXT, font=("Consolas", 14), fg=MAIN_FRAME_COLOR, justify="center")

compareTimenBtn = tk.Button(dataFrame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text="Сравнения времени", font=("Consolas", 14),
                            command=lambda: timeInput(1))
compareGradationBtn = tk.Button(dataFrame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text="Сравнения ступенчатости", font=("Consolas", 14),
                                command=lambda: timeInput(2))
clearCanvasBtn = tk.Button(dataFrame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text="Очистить экран", font=("Consolas", 14), command=clearScreen)
infoBtn = tk.Button(dataFrame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text="Справка", font=("Consolas", 14),
                    command=show_info)

lineLengthLabel.pack(fill='both', expand=True, side='top')
lengthEntry.pack(fill='both', expand=True, side='top')
compareTimenBtn.pack(fill='both', expand=True, side='top')
compareGradationBtn.pack(fill='both', expand=True, side='top')
clearCanvasBtn.pack(fill='both', expand=True, side='top')
infoBtn.pack(fill='both', expand=True, side='top')

#---------------------------------------------------------------------------------------------------------------
angleEntry.insert(0, str(15))
lengthEntry.insert(0, str(100))

xsEntry.insert(0, str(545))
ysEntry.insert(0, str(350))

xeEntry.insert(0, str(695))
yeEntry.insert(0, str(500))

drawAxes()



#--------------------
#set size of window
root.minsize(WINDOW_WIDTH * 3 // 4, WINDOW_HEIGHT * 3 // 4)
root.maxsize(WINDOW_WIDTH * 3//2, WINDOW_HEIGHT*3//2)
#-------------------------
root.mainloop()