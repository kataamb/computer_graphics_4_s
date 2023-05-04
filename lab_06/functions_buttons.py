# функций и кнопок стало так много, что пришлось вынести в отдельный файл...

import copy
import time
from tkinter import colorchooser as color_chooser, messagebox

import tkinter as tk
import interface as inter
import tkinter.messagebox as box
import tkinter.colorchooser as color_chooser



# ------------------------------------------------------------------------------------------------------------------------
def clear_screen(allFigures, currentFigure, actions_frame, canvas_frame, listbox_frame):
    allFigures.clear()
    currentFigure.clear()
    canvas_frame.redraw_canva()
    #actions_frame.keyboard_frame.points_list_box.delete(0, tk.END)
    #listbox_frame.

def set_color_screen(color_frame, canva_frame):
    canva = canva_frame.get_canva()
    color_code = color_chooser.askcolor(title="Choose color background canvas")
    canva.config(bg = color_code[-1])

def set_color_line(color_frame, canva_frame):
    color_code = color_chooser.askcolor(title="Choose color background canvas")
    canva_frame.line_color = color_code[-1]
    color_frame.cur_line_color_label.config(bg = color_code[-1])
    color_frame.set_line_color(color_code[-1])

#----------------------------------------------------------------------------------------------