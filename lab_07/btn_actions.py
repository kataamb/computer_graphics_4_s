import tkinter as tk
from tkinter import colorchooser as color_chooser, messagebox

import copy

from draw import add_line, draw_rectangle, click_right, draw_rectangle_by_Button
from alg_cut import sutherland_cohen_algorithm



#------------------------------------------------------------------------

def set_color_cut(color_frame):
    color_code = color_chooser.askcolor(title="Choose color cutter")
    color_frame.set_cut_color(color_code[-1])

def set_color_line(color_frame):
    color_code = color_chooser.askcolor(title="Choose color line")
    color_frame.cur_line_color_label.config(bg = color_code[-1])
    color_frame.set_line_color(color_code[-1])

def set_color_vis(color_frame):
    color_code = color_chooser.askcolor(title="Choose color of visible lines")
    color_frame.cur_visline_color_label.config(bg=color_code[-1])
    color_frame.set_vis_color(color_code[-1])
#-------------------------------------------------------------------------
def draw_line(line_frame, canva, lines, color):
    coord = line_frame.get_coordinates()
    if not(coord):
        return
    xStart, yStart, xEnd, yEnd = coord
    add_line(canva, lines, xStart, yStart, xEnd, yEnd, color)


def draw_clipper(cut_frame, canva, lines, rectangle, color):
    coord = cut_frame.get_coordinates()
    if not (coord):
        return
    xl, yl, xr, yr = coord
    rectangle[0] = xl
    rectangle[1] = yl
    rectangle[2] = xr
    rectangle[3] = yr

    draw_rectangle(canva, rectangle, lines, color)
#-------------------------------------------------------------------------
def click_left_motion(event, cutter, lines, canvasField, cutter_color):
    cutter.is_set_rectangle = draw_rectangle_by_Button(event, cutter.rectangle, lines, canvasField, cutter_color, cutter.is_set_rectangle)
# right: in draw file
#_________________________________________________________________________________--
CANVAS_COLOUR = "white"
def cut_off_command(canva, lines, cutter, color_frame):
    if cutter.rectangle[0] == -1:
        messagebox.showinfo("Ошибка", "Отсутствует отсекатель")

    rect = [min(cutter.rectangle[0], cutter.rectangle[2]), max(cutter.rectangle[0], cutter.rectangle[2]),
            min(cutter.rectangle[1], cutter.rectangle[3]), max(cutter.rectangle[1], cutter.rectangle[3])]

    color = color_frame.get_vis_color()

    canva.create_rectangle(rect[0] + 1, rect[2] + 1, rect[1] - 1, rect[3] - 1,
                                                        fill=CANVAS_COLOUR, outline=CANVAS_COLOUR) #CANVAS_COLOUR
    for line in lines:
        if line:
            pr, n_line = sutherland_cohen_algorithm(rect, line)
            if pr == 1 or pr == 0:
                canva.create_line(n_line[0][0], n_line[0][1], n_line[1][0], n_line[1][1], fill=color) #RESULT_COLOUR

#_________________________________________________________________________________
def add_vert_horiz_lines(rectangle, lines, canvas, colour):
    if rectangle[0] == -1:
        messagebox.showerror("Ошибка", "Отсутствует отсекатель")
        return

    x1 = rectangle[0]
    y1 = rectangle[1]
    x2 = rectangle[2]
    y2 = rectangle[3]

    dy = y2 - y1
    dx = x2 - x1

    lines.append([[x1, y1 + 0.1 * dy], [x1, y2 - 0.1 * dy], colour])
    lines.append([[x1 + 0.1 * dx, y1], [x2 - 0.1 * dx, y1], colour])

    canvas.create_line(x1, y1 + 0.1 * dy, x1, y2 - 0.1 * dy, fill=colour)
    canvas.create_line(x1 + 0.1 * dx, y1, x2 - 0.1 * dx, y1, fill=colour)

#----------------------------------------------------------------------------------
def clear_canvas(canva_frame, lines, cutter):
    canva_frame.redraw_canva()
    lines.clear()
    cutter.is_set_rectangle = False
    for i in range(4):
        cutter.rectangle[i] = -1
