import math
import tkinter as tk
from tkinter import ttk, messagebox


Font = ('Arial', 12)
FontHeader = ('Arial', 12)


class MainFrame(tk.Frame):
    def __init__(self, root, expand = False, color = None):
        self.root = root
        self.color = color
        self.expand = expand
        super().__init__(root)
        self.frame_configurations()

    def frame_configurations(self):
        self.pack(fill='both', expand=self.expand, side='right')

        if self.color:
            self.config(bg=self.color)


#####################################################################

class CanvasFrame(MainFrame):
    def __init__(self, root, expand = True,  color=None):
        self.color = color
        super().__init__(root, expand, color)
        self.canva = tk.Canvas(self, scrollregion=(-1000,-1000,1000,1000))
        #self.canva.bind(MOUSE_LEFT, self.get_point_canva)
        self.line_color = 'black'

        # config Canvas to be scrollable
        #self.make_canva_scrollable()

        self.canvas_interface()


    def canvas_interface(self):
        #self.canva.pack(fill='both', expand=True, side='left')
        self.canva.pack(side='left', expand=True, fill='both')
        self.canva.config(bg = 'white')
        self.redraw_canva()

    def make_canva_scrollable(self):
        '''
        config Canvas to be scrollable
        '''
        hbar = tk.Scrollbar(self, orient='horizontal')
        hbar.pack(side='bottom', fill='x')
        hbar.config(command=self.canva.xview)
        vbar = tk.Scrollbar(self, orient='vertical')
        vbar.pack(side='left', fill='y')
        vbar.config(command=self.canva.yview)

        self.canva.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)



    def get_canva(self):
        return self.canva

    def draw_axes(self): # !!!!!!!!
        CANVAS_XB = -1000
        CANVAS_YB = -1000
        CANVAS_XE = 1000
        CANVAS_YE = 1000
        color = 'gray'
        self.canva.create_line(CANVAS_XB + 3, 0, CANVAS_XE + 3, 0, width=2, fill='light gray', arrow=tk.LAST)
        self.canva.create_line(0, CANVAS_YB + 3, 0, CANVAS_YE + 3, width=2, fill='light gray', arrow=tk.LAST)
        for i in range(CANVAS_XB + 50, CANVAS_XE, 50):
            self.canva.create_text(i, 15, text=str(i), fill=color)
            self.canva.create_line(i, 0, i, 5, fill=color)

        for i in range(CANVAS_YB + 50, CANVAS_YE, 50):
            self.canva.create_text(20, i, text=str((i)), fill=color)
            self.canva.create_line(0, i, 5, i, fill=color)


    def redraw_canva(self):
        self.canva.delete("all")
        #self.draw_axes()

    def get_point_canva(self, event):
        x = event.x
        y = event.y



######################################################################################################################
class OptionFrame(tk.Frame):
    def __init__(self, parent_frame, name = 'Option', color = None, text_color = 'black'):
        self.parent_frame = parent_frame
        self.color = color
        self.name = name
        self.name_color = text_color
        super().__init__(parent_frame)
        self.option_configurations()

    def option_configurations(self):
        label_name = tk.Label(self, text = self.name, bg = 'lightslategray',
                              fg = self.name_color, font = FontHeader)
        label_name.pack(fill = 'x', side = 'top')
        self.pack(fill='both', expand = True, side='top')
        if self.color:
            self.config(bg=self.color)
        self.config(highlightbackground="black", highlightthickness=1)



class ColorFrame(OptionFrame):
    def __init__(self, parent_frame, name = 'Option',
             color = 'darkslategray', text_color = 'white'):

        super().__init__(parent_frame, name, color, text_color)
        self.color = color
        self.text_color = text_color

        self.line_color = 'black'
        self.cut_color = "blue"
        self.vis_color = 'red'


        self.color_line_frame = tk.Frame(self, bg = self.color)
        self.chng_line = tk.Button(self.color_line_frame, text = 'Изменить цвет отрезка', bg=self.color,
                                   font=Font, fg= text_color)
        self.line_label = tk.Label(self.color_line_frame, bg=self.color, text="Текущий цвет отрезка:",
                                   fg=text_color,   font=Font)
        self.cur_line_color_label = tk.Label(self.color_line_frame, bg="black")

        self.color_visline_frame = tk.Frame(self, bg=self.color)
        self.chng_visline = tk.Button(self.color_visline_frame, text='Изменить цвет видимых', bg=self.color,
                                     font=Font, fg=text_color)
        self.visline_label = tk.Label(self.color_visline_frame, bg=self.color, text="Текущий цвет видимых:",
                                     fg=text_color, font=Font)
        self.cur_visline_color_label = tk.Label(self.color_visline_frame, bg="red")

        self.cutting_color_frame = tk.Frame(self, bg=self.color)
        self.chng_cutting = tk.Button(self.cutting_color_frame, text='Изменить цвет отсекателя', bg=self.color,
                                      font=Font, fg=text_color)
        self.cutting_label = tk.Label(self.cutting_color_frame, bg=self.color, text="Текущий цвет отсекателя",
                                      fg=text_color, font=Font)
        self.cur_filling_color_label = tk.Label(self.cutting_color_frame, bg="black")

        self.color_interface()

    def color_interface(self):
        self.color_visline_frame.pack(side = 'top')
        self.chng_visline.pack(side = 'left', padx = 10, pady = 5)
        self.visline_label.pack(side='left', padx=10, pady=5)
        self.cur_visline_color_label.pack(side='left', padx=10, pady=5, fill='x', expand='true')

        self.color_line_frame.pack(side = 'top', expand = True)
        self.chng_line.pack(side = 'left', padx=10, pady=5)
        self.line_label.pack(side = 'left', padx=10, pady=5)
        self.cur_line_color_label.pack(side = 'left', padx=10, pady=5, fill = 'x', expand = 'true')

        self.cutting_color_frame.pack(side = 'top')
        self.chng_cutting.pack(side = 'left', padx=10, pady=5)
        self.cutting_label.pack(side = 'left', padx=10, pady=5)
        self.cur_filling_color_label.pack(side = 'left', padx=10, pady=5, fill = 'x', expand = 'true')


    def set_line_color(self, color):
        self.line_color = color

    def set_vis_color(self, color):
        self.vis_color = color

    def set_cut_color(self, color):
        self.line_color = color


    def get_line_color(self):
        return self.line_color

    def get_cut_color(self):
        return self.cut_color

    def get_vis_color(self):
        return self.vis_color



class KeyboardInputFrame(OptionFrame):
    def __init__(self, parent_frame, name = 'Option', color = 'darkslategray', text_color = 'white'):
        super().__init__(parent_frame, name, color, text_color)
        self.color = color
        self.text_color = text_color

        self.xb = tk.StringVar()
        self.yb = tk.StringVar()

        self.xe = tk.StringVar()
        self.ye = tk.StringVar()


        self.coord_frame = tk.Frame(self)
        self.btns_frame = tk.Frame(self)

        self.coord_xb = tk.Frame(self.coord_frame)
        self.point_xb = tk.Entry(self.coord_xb, textvariable=self.xb)

        self.coord_yb = tk.Frame(self.coord_frame)
        self.point_yb = tk.Entry(self.coord_yb, textvariable=self.yb)

        self.coord_xe = tk.Frame(self.coord_frame)
        self.point_xe = tk.Entry(self.coord_xe, textvariable=self.xe)

        self.coord_ye = tk.Frame(self.coord_frame)
        self.point_ye = tk.Entry(self.coord_ye, textvariable=self.ye)

        self.btn_line = tk.Button(self.btns_frame, text='Построить отрезок')

        self.all_interface()

    def all_interface(self):
        self.pack_interface()
        self.coordinates_interface()
        self.btns_interface()


    def pack_interface(self):
        self.coord_frame.config(bg=self.color) #self.color
        self.coord_frame.pack(fill='both', expand=False, side='top')

        self.btns_frame.config(bg=self.color)
        self.btns_frame.pack(fill='both', expand=False, side='top')


    def coordinates_interface(self):

        #create and pack labels
        frames_and_labels= { self.coord_xb : "Xbeg:", self.coord_yb : "Ybeg:",
                             self.coord_xe : "Xend:", self.coord_ye : "Yend:"}
        for frame in frames_and_labels:
            frame.pack(fill='both', expand=True, side='left')
            label = tk.Label(frame, text = frames_and_labels.get(frame), bg=self.color, font = Font, fg = 'white')
            label.pack(side='top', expand=True, fill='both')

        #pack entries
        entries = [self.point_xb, self.point_yb,
                              self.point_xe, self.point_ye]
        for entr in entries:
            entr.pack(fill='both', expand=False, side='top')


    def btns_interface(self):
        self.btn_line.config(bg=self.color, font=Font, fg=self.text_color)
        self.btn_line.pack(fill='both', expand=True, side='bottom')

    def get_coordinates(self):
        xStart = self.point_xb.get()
        yStart = self.point_yb.get()
        xEnd = self.point_xe.get()
        yEnd = self.point_ye.get()

        if not xStart or not yStart:
            messagebox.showwarning('Ошибка ввода',
                                   'Не заданы координаты начала отрезка!')
        elif not xEnd or not yEnd:
            messagebox.showwarning('Ошибка ввода',
                                   'Не заданы координаты конца отрезка!')
        else:
            try:
                xStart, yStart = int(xStart), int(yStart)
                xEnd, yEnd = int(xEnd), int(yEnd)
            except all:
                messagebox.showwarning('Ошибка ввода',
                                       'Координаты заданы неверно!')
                return ()
        return (xStart, yStart, xEnd, yEnd)




class KeyboardInputCutFrame(OptionFrame):
    def __init__(self, parent_frame, name = 'Option', color = 'darkslategray', text_color = 'white'):
        super().__init__(parent_frame, name, color, text_color)
        self.color = color
        self.text_color = text_color

        self.xb = tk.StringVar()
        self.yb = tk.StringVar()

        self.xe = tk.StringVar()
        self.ye = tk.StringVar()


        self.coord_frame = tk.Frame(self)
        self.btns_frame = tk.Frame(self)

        self.coord_xb = tk.Frame(self.coord_frame)
        self.point_xb = tk.Entry(self.coord_xb, textvariable=self.xb)

        self.coord_yb = tk.Frame(self.coord_frame)
        self.point_yb = tk.Entry(self.coord_yb, textvariable=self.yb)

        self.coord_xe = tk.Frame(self.coord_frame)
        self.point_xe = tk.Entry(self.coord_xe, textvariable=self.xe)

        self.coord_ye = tk.Frame(self.coord_frame)
        self.point_ye = tk.Entry(self.coord_ye, textvariable=self.ye)

        self.btn_line = tk.Button(self.btns_frame, text='Построить отсекатель')

        self.all_interface()

    def all_interface(self):
        self.pack_interface()
        self.coordinates_interface()
        self.btns_interface()


    def pack_interface(self):
        self.coord_frame.config(bg=self.color) #self.color
        self.coord_frame.pack(fill='both', expand=False, side='top')

        self.btns_frame.config(bg=self.color)
        self.btns_frame.pack(fill='both', expand=False, side='top')


    def coordinates_interface(self):

        #create and pack labels
        frames_and_labels= { self.coord_xb : "Xлв:", self.coord_yb : "Yлв:",
                             self.coord_xe : "Xпн:", self.coord_ye : "Yпн:"}
        for frame in frames_and_labels:
            frame.pack(fill='both', expand=True, side='left')
            label = tk.Label(frame, text = frames_and_labels.get(frame), bg=self.color, font = Font, fg = 'white')
            label.pack(side='top', expand=True, fill='both')

        #pack entries
        entries = [self.point_xb, self.point_yb,
                              self.point_xe, self.point_ye]
        for entr in entries:
            entr.pack(fill='both', expand=False, side='top')


    def btns_interface(self):
        self.btn_line.config(bg=self.color, font=Font, fg=self.text_color)
        self.btn_line.pack(fill='both', expand=True, side='bottom')

    def get_coordinates(self):
        xStart = self.point_xb.get()
        yStart = self.point_yb.get()
        xEnd = self.point_xe.get()
        yEnd = self.point_ye.get()

        if not xStart or not yStart:
            messagebox.showwarning('Ошибка ввода',
                                   'Не заданы координаты верхнего угла отсекателя!')
        elif not xEnd or not yEnd:
            messagebox.showwarning('Ошибка ввода',
                                   'Не заданы координаты нижнего угла отсекателя!')
        else:
            try:
                xStart, yStart = int(xStart), int(yStart)
                xEnd, yEnd = int(xEnd), int(yEnd)
            except all:
                messagebox.showwarning('Ошибка ввода',
                                       'Координаты заданы неверно!')
                return ()
        return (xStart, yStart, xEnd, yEnd)



class MouseInputFrame(OptionFrame):
    def __init__(self, parent_frame, name = 'Option', color = 'darkslategray', text_color = 'white'):
        super().__init__(parent_frame, name, color, text_color)
        self.color = color
        self.text_color = text_color

        self.btn_circle_time = tk.Label(self, text = 'Добавить отрезок - левая кнопка мыши')
        self.btn_ellips_time = tk.Label(self, text = 'Добавить отсекатель - правая кнопка мыши')
        #self.lbl_seed_point = tk.Label(self, text='Добавить затравочную точку - ...')

        self.analyzis_interface()

    def analyzis_interface(self):
        self.btn_circle_time.config(bg = self.color, font = Font, fg = self.text_color)
        self.btn_circle_time.pack(side = 'top', expand = True, fill = 'x')
        self.btn_ellips_time.config(bg=self.color, font=Font, fg=self.text_color)
        self.btn_ellips_time.pack(side = 'top', expand = True, fill = 'x')
        #self.lbl_seed_point.config(bg=self.color, font=Font, fg=self.text_color)
        #self.lbl_seed_point.pack(side='top', expand=True, fill='x')




class AnalyzisFrame(OptionFrame):
    def __init__(self, parent_frame, name = 'Option', color = 'darkslategray', text_color = 'white'):
        super().__init__(parent_frame, name, color, text_color)
        self.color = color
        self.text_color = text_color

        self.lbl_time = tk.Label(self)

        self.analyzis_interface()

    def analyzis_interface(self):
        self.lbl_time_info = tk.Label(self, text = 'Время закраски:')
        self.lbl_time_info.config(bg=self.color, font=Font, fg=self.text_color)
        self.lbl_time_info.pack(side='left', expand=True, fill='x')

        self.lbl_time.config(bg = self.color, font = Font, fg = self.text_color)
        self.lbl_time.pack(side='left', expand=True, fill='x')

    def set_time(self, string):
        self.lbl_time.config(text = string)



##################################################################################################

class ActionsFrame(MainFrame):
    def __init__(self, root, color=None):
        self.color = color
        super().__init__(root)

        self.Figures = []

        self.color_frame = ColorFrame(self, 'Цвета')
        self.keyboard_particle_frame = KeyboardInputFrame(self, 'Ввод с клавиатуры: отрезок')
        self.keyboard_cut_frame = KeyboardInputCutFrame(self, 'Ввод с клавиатуры: отсекатель')
        self.mouse_frame = MouseInputFrame(self, 'Ввод мышью')

        self.btn_cut = tk.Button(self, text='Отсечь', bg='darkslategray', fg='white', font=('Arial', 20))
        self.btn_add_line = tk.Button(self, text='Добавить параллельные \n отсекателю отрезки',
                                      bg='darkslategray', fg='white', font=('Arial', 20))

        self.btn_clear = tk.Button(self, text='Очистить', bg='darkslategray', fg='white', font=('Arial', 20))
        self.btn_info = tk.Button(self, text='Справка', bg = 'darkslategray', fg = 'white', font = ('Arial', 20))

        self.actions_interface()



    def actions_interface(self):
        self.btn_cut.pack(fill='both', expand=False, side='top')
        self.btn_add_line.pack(fill='both', expand=False, side='top')
        self.btn_clear.pack(fill='both', expand=False, side='top')
        self.btn_info.pack(fill='both', expand=False, side='top')


    def print_info(self):
        messagebox.showinfo('Информация',
                        'С помощью данной программы можно построить фигуру и закрасить ее:\n'
                        '\nДля построения закраски фигуры используется алгоритм с упорядоченным списоком ребер \n'
                        'и его реализация с помощью списка рёбер.\n'
                     "\nАвтор: Амбарцумова Екатерина, ИУ7-45Б\n"
                            )

    def clear_drawing(self):
        self.drawing_field.redraw_canva()





