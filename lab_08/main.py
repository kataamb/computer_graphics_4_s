import tkinter as tk
import interface as inter
import tkinter.messagebox as box
import tkinter.colorchooser as color_chooser

from btn_actions import*

WIDTH = 1400
HEIGHT = 800

MOUSE_LEFT = '<1>'
MOUSE_RIGHT = '<Button-3>'

class Cutter():
    rectangle = [-1, -1, -1, -1]
    is_set_rectangle = False

if __name__ == '__main__':

    lines = []
    cutter = Cutter()

    main_window = tk.Tk()
    main_window.geometry("{}x{}+1+5".format(WIDTH, HEIGHT))

    main_window.minsize(WIDTH * 3 // 4, HEIGHT * 3 // 4)
    main_window.maxsize(WIDTH * 3//2, HEIGHT*3//2)

    output_part = inter.CanvasFrame(main_window)
    actions_part = inter.ActionsFrame(main_window)


    # config buttons with actions(functions)
    #actions_part.btn_clear.config(command=lambda: clear_screen(allFigures, currentFigure, actions_part, output_part, list_part))
    #actions_part.btn_info.config(command=lambda: actions_part.print_info())


    main_window.title("ЛР7")
    main_window.mainloop()