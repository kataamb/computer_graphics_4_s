import tkinter as tk
import interface as inter
import tkinter.messagebox as box
import tkinter.colorchooser as color_chooser

WIDTH = 1400
HEIGHT = 800

def set_color_screen(color_frame, canva_frame):
    canva = canva_frame.get_canva()
    color_code = color_chooser.askcolor(title="Choose colour background canvas")
    canva.config(bg = color_code[-1])

def set_color_line(color_frame, canva_frame):
    color_code = color_chooser.askcolor(title="Choose colour background canvas")
    canva_frame.line_color = color_code[-1]
    color_frame.cur_line_color_label.config(bg = color_code[-1])
    color_frame.set_line_color(color_code[-1])

'''
main function to process all data, got on actions frame
and output to canvas frame (draw) (output_part)
'''

if __name__ == '__main__':
    main_window = tk.Tk()
    main_window.geometry("{}x{}+1+5".format(WIDTH, HEIGHT))

    main_window.minsize(WIDTH * 3 // 4, HEIGHT * 3 // 4)
    main_window.maxsize(WIDTH * 3//2, HEIGHT*3//2)

    output_part = inter.CanvasFrame(main_window)
    actions_part = inter.ActionsFrame(main_window)

    # config buttons with actions(functions)
    actions_part.color_frame.chng_screen.config(command = lambda: set_color_screen(actions_part.color_frame, output_part))
    actions_part.color_frame.chng_line.config(command=lambda: set_color_line(actions_part.color_frame, output_part))

    actions_part.btn_clear.config(command = lambda: output_part.redraw_canva())
    actions_part.btn_info.config(command=lambda: actions_part.print_info())




    main_window.title("ЛР5")
    main_window.mainloop()