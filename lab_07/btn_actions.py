import tkinter as tk
from tkinter import colorchooser, messagebox

import copy

from draw import add_line, draw_rectangle, click_right, draw_rectangle_by_Button
from alg_cut import sutherland_cohen_algorithm



#-------------------------------------------------------------------------
def drawLine(line_frame, canva, lines, color):
    coord = line_frame.get_coordinates()
    if not(coord):
        return
    xStart, yStart, xEnd, yEnd = coord
    add_line(canva, lines, xStart, yStart, xEnd, yEnd, color)

def drawClipper(cut_frame, canva, lines, rectangle, color):
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
def click_left_motion(event, is_set_rectangle, cutting,  lines, canvasField, line_color):
    return draw_rectangle_by_Button(event, cutting, lines, canvasField, line_color, is_set_rectangle)


def clear_canvas(canva, lines, rectangle):
    canva.delete("all")
    lines.clear()
    is_set_rectangle = False
    for i in range(4):
        rectangle[i] = -1
    return is_set_rectangle