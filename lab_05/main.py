
import tkinter as tk
import interface as inter
import tkinter.messagebox as box
import tkinter.colorchooser as color_chooser

from algrorithm import CAP_algorithm_with_ordered_list_of_edges, Point
import tkinter as tk
from tkinter import colorchooser, messagebox
from config import *

from point import*
import time

WIDTH = 1400
HEIGHT = 800

MOUSE_LEFT = '<1>'
MOUSE_RIGHT = '<Button-3>'

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

def clear_screen(allFigures, currentFigure, actions_frame, canvas_frame):
    allFigures.clear()
    currentFigure.clear()
    canvas_frame.redraw_canva()
    actions_frame.keyboard_frame.points_list_box.delete(0, tk.END)



def fill_all_figures(allFigures, currentFigure, actions_frame, canvas_frame):
    if not allFigures and not currentFigure:
        messagebox.showwarning("Предупреждение!", "Фигура не введена для закраски!")
    elif not allFigures and  currentFigure:
        messagebox.showwarning("Предупреждение!", "Фигура не замкнута для закраски!")
    else:
        delay = False
        if methodDraw.get() == 0:
            delay = True
        time_start = time.time()
        CAP_algorithm_with_ordered_list_of_edges(canvasField, allFigures, colour=LINE_COLOUR, delay=delay)
        time_end = time.time() - time_start
        if round(time_end * 1000, 2) < 1000:
            timeLabel["text"] = "Время закраски: " + str(round(time_end * 1000, 2)) + " mc."
        else:
            timeLabel["text"] = "Время закраски: " + str(round(time_end, 2)) + " c."



#---------------------------------------------------------------------------------------------

def findIndexForListPointScroll(allArraysFigure, currentArray):
    index = 0

    for pointFigure in allArraysFigure:
         index += len(pointFigure) + 1

    index += len(currentArray)
    return len(currentArray)

def add_point(x, y, allFigures, currentFigure, points_frame, canva_frame):
    if Point(x, y) not in currentFigure:
        # canvasField.create_text(x, y - 10, text=(str(x) + " " + str(y)))
        if currentFigure:
            canva_frame.canva.create_line(currentFigure[-1].x, currentFigure[-1].y, x, y)

        index = findIndexForListPointScroll(allFigures, currentFigure)
        points_frame.points_list_box.insert(tk.END,  "{:3d}) X = {:4d}; Y = {:4d}".format(index + 1, x, y))
        currentFigure.append(Point(x, y))
    else:
        messagebox.showwarning("Предупреждение!", "Точка с такими координатами фигуры уже введена!")
# ------------------------------------------------------------------------------------------------------------------------

def set_color_screen(color_frame, canva_frame):
    canva = canva_frame.get_canva()
    color_code = color_chooser.askcolor(title="Choose color background canvas")
    canva.config(bg = color_code[-1])

def set_color_line(color_frame, canva_frame):
    color_code = color_chooser.askcolor(title="Choose color background canvas")
    canva_frame.line_color = color_code[-1]
    color_frame.cur_line_color_label.config(bg = color_code[-1])
    color_frame.set_line_color(color_code[-1])


def get_point_canvas(event, allFigures, currentFigure, points_frame, canva_frame):
    x, y = event.x, event.y
    add_point(x, y, allFigures, currentFigure, points_frame, canva_frame)

    if (len(points_frame.points) > 1):
        canva_frame.canva.create_line(points_frame.points[-2][0], points_frame.points[-2][1],
                                      points_frame.points[-1][0], points_frame.points[-1][1])


def get_point_keyboard(allFigures, currentFigure, points_frame, canva_frame):
    pair = points_frame.get_coordinate()
    if pair == 0:
        return
    x, y = pair
    x, y = int(x), int(y)

    add_point(x, y, allFigures, currentFigure, points_frame, canva_frame)




def connect_figure_canvas(event, allFigures, currentFigure, points_frame, canva_frame):
    if len(currentFigure) > 2:
        canva_frame.canva.create_line(currentFigure[-1].x, currentFigure[-1].y,
                                      currentFigure[0].x, currentFigure[0].y)

        points_frame.points_list_box.insert(tk.END, "------------Closed------------")

        allFigures.append(currentFigure)
        currentFigure.clear()
    elif len(currentFigure) == 0:
        messagebox.showwarning("Предупреждение!", "Точки фигуры не введены!")
    else:
        messagebox.showwarning("Предупреждение!",
                               "Такую фигуру нельзя замкнуть!\nНеобходимо как минимум, чтобы у фигуры было 3 точки!")



def connect_figure_keyboard(allFigures, currentFigure, points_frame, canva_frame):
    if len(currentFigure) > 2:
        canva_frame.canva.create_line(currentFigure[-1].x, currentFigure[-1].y,
                                      currentFigure[0].x, currentFigure[0].y)

        points_frame.points_list_box.insert(tk.END, "------------Closed------------")

        allFigures.append(currentFigure)
        currentFigure.clear()
    elif len(currentFigure) == 0:
        messagebox.showwarning("Предупреждение!", "Точки фигуры не введены!")
    else:
        messagebox.showwarning("Предупреждение!",
                               "Такую фигуру нельзя замкнуть!\nНеобходимо как минимум, чтобы у фигуры было 3 точки!")


'''
main function to process all data, got on actions frame
and output to canvas frame (draw) (output_part)
'''

if __name__ == '__main__':

    currentFigure = []
    allFigures = []

    main_window = tk.Tk()
    main_window.geometry("{}x{}+1+5".format(WIDTH, HEIGHT))

    main_window.minsize(WIDTH * 3 // 4, HEIGHT * 3 // 4)
    main_window.maxsize(WIDTH * 3//2, HEIGHT*3//2)

    output_part = inter.CanvasFrame(main_window)
    actions_part = inter.ActionsFrame(main_window)

    # config buttons with actions(functions)
    actions_part.color_frame.chng_screen.config(command = lambda: set_color_screen(actions_part.color_frame, output_part))
    actions_part.color_frame.chng_line.config(command=lambda: set_color_line(actions_part.color_frame, output_part))

    actions_part.keyboard_frame.btn_add_point.config(command = lambda: add_point(allFigures, currentFigure, actions_part.keyboard_frame, output_part))
    actions_part.keyboard_frame.btn_connect_figure.config(
        command=lambda: connect_figure_keyboard(allFigures, currentFigure, actions_part.keyboard_frame, output_part))

    output_part.canva.bind(MOUSE_LEFT,
                lambda event, frame = actions_part.keyboard_frame,
                canvas = output_part: get_point_canvas(event, allFigures, currentFigure, frame, canvas))
    output_part.canva.bind(MOUSE_RIGHT,
                           lambda event, frame = actions_part.keyboard_frame,
                                canvas = output_part: connect_figure_canvas(event, allFigures, currentFigure, frame, canvas))

    actions_part.btn_clear.config(command = lambda: clear_screen(allFigures, currentFigure, actions_part, output_part))
    actions_part.btn_info.config(command=lambda: actions_part.print_info())




    main_window.title("ЛР5")
    main_window.mainloop()
