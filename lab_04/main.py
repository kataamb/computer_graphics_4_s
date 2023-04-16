import tkinter as tk
import interface as inter
import tkinter.messagebox as box
import tkinter.colorchooser as color_chooser

from bresenham import bresenham_circle_octant, bresenham_ellipse
from canonic import canonical_сircle, canonical_ellipse
from parametric import parameter_circle, parameter_ellipse
from midpoint import midpoint_circle, midpoint_ellipse

from measure_time import time_comparison, drawAxes


import draw_algorithms as draw

WIDTH = 1400
HEIGHT = 800



def define_alg_by_id(alg_id, mode):
    if mode == 'circle':
        if alg_id == '1':
            return canonical_сircle
        if alg_id == '2':
            return parameter_circle
        if alg_id == '3':
            return bresenham_circle_octant
        if alg_id == '4':
            return midpoint_circle
        else:
            return draw.standard_circle
    if mode == 'ellipse':
        if alg_id == '1':
            return canonical_ellipse
        if alg_id == '2':
            return parameter_ellipse
        if alg_id == '3':
            return bresenham_ellipse
        if alg_id == '4':
            return midpoint_ellipse
        else:
            return draw.standard_oval



def draw_circle(actions, output):
    center = actions.ellips_frame.get_center()
    if not(center !=0 ):
        return
    radius = actions.ellips_frame.get_radius()
    if not(radius !=0 ):
        return
    alg_id = actions.algos_frame.get_algorithm()
    if not (radius != 0):
        return
    algorithm = define_alg_by_id(alg_id, 'circle')
    if not(algorithm !=0):
        return
    canva = output.get_canva()
    if not(canva !=0 ):
        return
    color = actions.color_frame.get_line_color()
    if not(color !=0):
        return

    draw.circle_by_algotithm(canva, algorithm, center[0], center[1], radius, color)

def draw_ellipse(actions, output):
    center = actions.ellips_frame.get_center()
    if not(center !=0 ):
        return
    ab = actions.ellips_frame.get_ellipse_parameters()
    if not(ab !=0):
        return
    alg_id = actions.algos_frame.get_algorithm()
    algorithm = define_alg_by_id(alg_id, 'ellipse')
    if not(algorithm !=0):
        return

    canva = output.get_canva()
    if not(canva !=0 ):
        return
    color = actions.color_frame.get_line_color()
    if not(color !=0):
        return

    draw.ellipse_by_algotithm(canva, algorithm, center[0], center[1], ab[0], ab[1], color)

def draw_circle_spectrum(actions, output):
    center = actions.ellips_frame.get_center()
    if not (center != 0):
        return
    radius = actions.spectrum_frame.get_start_radius()
    if not (radius != 0):
        return
    alg_id = actions.algos_frame.get_algorithm()
    algorithm = define_alg_by_id(alg_id, 'circle')
    if not (algorithm != 0):
        return
    step = actions.spectrum_frame.get_step()
    if not (step != 0):
        return
    count = actions.spectrum_frame.get_number_figures()
    if not (count != 0):
        return
    canva = output.get_canva()
    if not (canva != 0):
        return
    color = actions.color_frame.get_line_color()
    if not (color != 0):
        return


    draw.spectrumCircleBy_algorith(canva, algorithm, center[0], center[1], radius, step, count, color)

def draw_ellipse_spectrum(actions, output):
    center = actions.ellips_frame.get_center()
    if not (center != 0):
        return
    ab = actions.spectrum_frame.get_start_ellipse_parameters()
    if not (ab != 0):
        return
    alg_id = actions.algos_frame.get_algorithm()
    algorithm = define_alg_by_id(alg_id, 'ellipse')
    if not (algorithm != 0):
        return
    step = actions.spectrum_frame.get_step()
    if not (step != 0):
        return
    count = actions.spectrum_frame.get_number_figures()
    if not (count != 0):
        return

    canva = output.get_canva()
    if not (canva != 0):
        return
    color = actions.color_frame.get_line_color()
    if not (color != 0):
        return

    draw.spectrumEllipseBy_algorith(canva, algorithm, center[0], center[1], ab[0], ab[1], step, count, color)


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

    actions_part.ellips_frame.btn_ellipses.config(command=lambda: draw_ellipse(actions_part, output_part))
    actions_part.ellips_frame.btn_circles.config(command=lambda: draw_circle(actions_part, output_part))

    actions_part.spectrum_frame.btn_ellipses.config(command=lambda: draw_ellipse_spectrum(actions_part, output_part))
    actions_part.spectrum_frame.btn_circles.config(command=lambda: draw_circle_spectrum(actions_part, output_part))

    actions_part.analyzis_frame.btn_circle_time.config(command=lambda: time_comparison(output_part.get_canva(), 'black', "circle"))
    actions_part.analyzis_frame.btn_ellips_time.config(command=lambda: time_comparison(output_part.get_canva(), 'black', "ellipse"))

    actions_part.btn_clear.config(command = lambda: output_part.redraw_canva())
    actions_part.btn_info.config(command=lambda: actions_part.print_info())



    main_window.title("ЛР4")
    main_window.mainloop()

