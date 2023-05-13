import tkinter as tk
from tkinter import colorchooser as color_chooser, messagebox

import copy

from draw import add_line, draw_rectangle, click_right, draw_rectangle_by_Button
from alg_cut import sutherland_cohen_algorithm



#------------------------------------------------------------------------

def set_color_cut(color_frame):
    color_code = color_chooser.askcolor(title="Choose color background canvas")
    color_frame.set_cut_color(color_code[-1])

def set_color_line(color_frame):
    color_code = color_chooser.askcolor(title="Choose color background canvas")
    color_frame.cur_line_color_label.config(bg = color_code[-1])
    color_frame.set_line_color(color_code[-1])

def set_color_vis(color_frame):
    color_code = color_chooser.askcolor(title="Choose color background canvas")
    color_frame.cur_visline_color_label.config(bg=color_code[-1])
    color_frame.set_vis_color(color_code[-1])
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
def click_left_motion(event, cutter, lines, canvasField, line_color):
    cutter.is_set_rectangle = draw_rectangle_by_Button(event, cutter.rectangle, lines, canvasField, line_color, cutter.is_set_rectangle)


def clear_canvas(canva, lines, cutter):
    canva.delete("all")
    lines.clear()
    cutter.is_set_rectangle = False
    for i in range(4):
        cutter.rectangle[i] = -1
