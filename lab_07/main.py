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
    #color set
    actions_part.color_frame.chng_line.config(command=lambda: set_color_line(actions_part.color_frame))
    actions_part.color_frame.chng_cutting.config(command=lambda: set_color_cut(actions_part.color_frame))
    actions_part.color_frame.chng_visline.config(command=lambda: set_color_vis(actions_part.color_frame))
    #keyboard
    actions_part.keyboard_particle_frame.btn_line.config(command=lambda:draw_line(
        actions_part.keyboard_particle_frame, output_part.canva, lines, actions_part.color_frame.get_line_color()))

    actions_part.keyboard_cut_frame.btn_line.config(command=lambda: draw_clipper(
        actions_part.keyboard_cut_frame, output_part.canva, lines, cutter.rectangle, actions_part.color_frame.get_cut_color()))
    #
    #mouse bind
    output_part.canva.bind("<Button-3>", lambda event: click_right(event, lines, output_part.canva,
                                                                   actions_part.color_frame.get_line_color()))
    output_part.canva.bind("<B1-Motion>", lambda event: click_left_motion(event, cutter, lines, output_part.canva,
                                                                          actions_part.color_frame.get_cut_color()))
    #options
    actions_part.btn_cut.config(command=lambda: cut_off_command(output_part.canva, lines, cutter, actions_part.color_frame))
    actions_part.btn_add_line.config(command=lambda: add_vert_horiz_lines(cutter.rectangle, lines, output_part.canva,
                                                                          actions_part.color_frame.get_line_color()))

    actions_part.btn_clear.config(command=lambda: clear_canvas(output_part, lines, cutter))
    actions_part.btn_info.config(command=lambda: actions_part.print_info())


    main_window.title("ЛР7")
    main_window.mainloop()