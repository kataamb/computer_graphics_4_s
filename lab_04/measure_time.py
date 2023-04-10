import time
from matplotlib import pyplot as plt
import numpy as np

from draw_algorithms import add_circle, add_ellipse
import tkinter as tk

MAIN_COLOUR = "#2b2b2b"
MAIN_FRAME_COLOR = "#313335"
MAIN_COLOUR_LABEL_BG = "purple"
MAIN_COLOUR_LABEL_TEXT = "white"
CANVAS_COLOUR = "lightblue"
LINE_COLOUR = "black"

COLUMNS = 35

WINDOW_WIDTH = 1900
WINDOW_HEIGHT = 1000

DATA_SITUATION = 1.1/4
BORDERS_SPACE = 10

DATA_FRAME_WIGHT = WINDOW_WIDTH * DATA_SITUATION - BORDERS_SPACE
DATA_FRAME_HEIGHT = WINDOW_HEIGHT - 2 * BORDERS_SPACE

CANVAS_SITUATION = 1 - DATA_SITUATION
CANVAS_WIDTH = WINDOW_WIDTH * CANVAS_SITUATION - 2 * BORDERS_SPACE
CANVAS_HEIGHT = WINDOW_HEIGHT - 2 * BORDERS_SPACE




NUMBER_OF_RUNS = 100
MAX_RADIUS = 10000
STEP = 1000


def drawAxes(canvas):
    color = 'gray'
    canvas.create_line(0, 3, CANVAS_WIDTH, 3, width=1, fill='gray', arrow=tk.LAST)
    canvas.create_line(3, 0, 3, CANVAS_HEIGHT, width=1, fill='gray', arrow=tk.LAST)
    for i in range(50, int(CANVAS_WIDTH), 50):
        canvas.create_text(i, 15, text=str(abs(i)), fill=color)
        canvas.create_line(i, 0, i, 5, fill=color)

    for i in range(50, int(CANVAS_HEIGHT), 50):
        canvas.create_text(20, i, text=str(abs(i)), fill=color)
        canvas.create_line(0, i, 5, i, fill=color)


def clearCanvas(canvas):
    canvas.delete("all")
    drawAxes(canvas)

def time_comparison(canvas, colour, figure):
    time_list = []

    xc = round(CANVAS_WIDTH // 2)
    yc = round(CANVAS_HEIGHT // 2)

    if figure != "ellipse" and figure != "circle":
        return

    for i in range(5):
        time_start = [0] * (MAX_RADIUS // STEP)
        time_end   = [0] * (MAX_RADIUS // STEP)

        for _ in range(NUMBER_OF_RUNS):
            ra = STEP
            rb = STEP

            for j in range(MAX_RADIUS // STEP):
                if figure == "ellipse" or figure == "circle":
                    time_start[j] += time.time()
                    add_ellipse(canvas, i, xc, yc, ra, rb, colour, drawMode=False)
                    time_end[j] += time.time()

                    rb += STEP
                elif figure == "_":
                    time_start[j] += time.time()
                    add_circle(canvas, i, xc, yc, ra, colour, drawMode=False)
                    time_end[j] += time.time()

                ra += STEP

            clearCanvas(canvas)

        size = len(time_start)
        res_time = list((time_end[i] - time_start[i]) / (NUMBER_OF_RUNS - 2) for i in range(size))
        time_list.append(res_time)

    radius_arr = list(i for i in range(STEP, MAX_RADIUS + STEP, STEP))

    if figure == "ellipse":
        figure = "эллипса"
    elif figure == "circle":
        figure = "окружности"

    plt.figure(figsize = (10, 6))
    plt.rcParams['font.size'] = '12'
    plt.title("Замеры времени для построения %s.\n" %(figure))

    plt.plot(radius_arr, time_list[0], label='Каноническое уравнение')
    plt.plot(radius_arr, time_list[1], label='Параметрическое уравнение')
    plt.plot(radius_arr, time_list[2], label='Алгоритм средней точки')
    plt.plot(radius_arr, time_list[3], label='Алгоритм Брезенхема')
    plt.plot(radius_arr, time_list[4], label='Библиотечная функция')

    plt.xticks(np.arange(STEP, MAX_RADIUS + STEP, STEP))
    plt.legend()
    plt.xlabel("Длина радиуса")
    plt.ylabel("Время")

    plt.show()
