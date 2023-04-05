
import tkinter as tk
import interface as inter
import tkinter.messagebox as box

WIDTH = 1000
HEIGHT = 800

'''
main function to process all data, got on actions frame
and output to canvas frame (draw) (output_part)
'''
def set_screen_color():
    print('Youre in f1')
def set_line_color():
    pass

def draw_circle():
    pass
def draw_ellipse():
    pass

def draw_circle_spectrum():
    pass
def draw_ellipse_spectrum():
    pass


def f1():
    print('here change screen color')

def f2():
    print('here change line color')

def set_color(color_frame, canva_frame):
    canva = canva_frame.get_canva()
    canva.config(bg = 'red')


if __name__ == '__main__':
    main_window = tk.Tk()
    main_window.geometry("{}x{}+1+5".format(WIDTH, HEIGHT))

    main_window.minsize(WIDTH * 3 // 4, HEIGHT * 3 // 4)
    main_window.maxsize(WIDTH * 3//2, HEIGHT*3//2)

    output_part = inter.CanvasFrame(main_window)
    actions_part = inter.ActionsFrame(main_window)

    actions_part.color_frame.chng_screen.config(command = lambda: set_color(actions_part.color_frame, output_part))


    #actions_part.color_frame.set_functions([f1, f2])






    #process(actions_part, output_part)



    main_window.title("ЛР4")
    main_window.mainloop()

