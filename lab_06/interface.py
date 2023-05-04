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
        self.make_canva_scrollable()

        self.canvas_interface()


    def canvas_interface(self):
        #self.canva.pack(fill='both', expand=True, side='left')
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
        self.canva.pack(side='left', expand=True, fill='both')


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
        self.draw_axes()

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

        self.color_screen_frame = tk.Frame(self, bg=self.color)
        self.chng_screen = tk.Button(self.color_screen_frame, text = 'Изменить цвет экрана', bg=self.color,
                                     font=Font, fg= text_color)
        self.screen_label = tk.Label(self.color_screen_frame, bg=self.color, text="Текущий цвет экрана:",
                                   fg=text_color, font=Font)
        self.cur_screen_color_label = tk.Label(self.color_screen_frame, bg="white")

        self.color_line_frame = tk.Frame(self, bg = self.color)
        self.chng_line = tk.Button(self.color_line_frame, text = 'Изменить цвет линии', bg=self.color,
                                   font=Font, fg= text_color)
        self.line_label = tk.Label(self.color_line_frame, bg=self.color, text="Текущий цвет линии:",
                                   fg=text_color,   font=Font)
        self.cur_line_color_label = tk.Label(self.color_line_frame, bg="black")

        self.filling_color_frame = tk.Frame(self, bg=self.color)
        self.chng_filling = tk.Button(self.filling_color_frame, text='Изменить цвет закраски', bg=self.color,
                                      font=Font, fg=text_color)
        self.filling_label = tk.Label(self.filling_color_frame, bg=self.color, text="Текущий цвет закраски:",
                                      fg=text_color, font=Font)
        self.cur_filling_color_label = tk.Label(self.filling_color_frame, bg="black")

        self.color_interface()

    def color_interface(self):
        self.color_screen_frame.pack(side = 'top')
        self.chng_screen.pack(side = 'left', padx = 10, pady = 5)
        self.screen_label.pack(side='left', padx=10, pady=5)
        self.cur_screen_color_label.pack(side='left', padx=10, pady=5, fill='x', expand='true')

        self.color_line_frame.pack(side = 'top', expand = True)
        self.chng_line.pack(side = 'left', padx=10, pady=5)
        self.line_label.pack(side = 'left', padx=10, pady=5)
        self.cur_line_color_label.pack(side = 'left', padx=10, pady=5, fill = 'x', expand = 'true')

        self.filling_color_frame.pack(side = 'top')
        self.chng_filling.pack(side = 'left', padx=10, pady=5)
        self.filling_label.pack(side = 'left', padx=10, pady=5)
        self.cur_filling_color_label.pack(side = 'left', padx=10, pady=5, fill = 'x', expand = 'true')


    def set_line_color(self, color):
        self.line_color = color


    def get_line_color(self):
        return self.line_color


class DrawingModeFrame(OptionFrame):
    def __init__(self, parent_frame, name = 'Option', color = 'darkslategray', text_color = 'white'):
        super().__init__(parent_frame, name, color, text_color)
        self.color = color
        self.text_color = text_color

        self.radio_btns_frame = tk.Frame(self)

        self.MODES = [('С задержкой', '1'), ('Без задержки', '2')]


        self.mode = tk.StringVar()
        self.mode.set("1")
        self.modes = self.create_modes_radios()

        self.drawing_modes_interface()

    def create_radio(self, option, frame):
        text, value = option
        return tk.Radiobutton(frame, bg = self.color, selectcolor = self.color,
                              text=text, value=value, variable=self.mode, font = Font, fg = 'white')

    def create_modes_radios(self):
        modes = []
        for i in self.MODES:
            modes.append( self.create_radio(i, self.radio_btns_frame))

        return modes

    def drawing_modes_interface(self):
        self.radio_btns_frame.config(bg = self.color)
        self.radio_btns_frame.pack(expand = True)
        for button in self.modes:
            button.pack(side = 'left', padx=10, pady=5)
            button.config(font = Font)

    def get_mode(self):
        return self.mode.get()



class KeyboardInputFrame(OptionFrame):
    def __init__(self, parent_frame, name = 'Option', color = 'darkslategray', text_color = 'white'):
        super().__init__(parent_frame, name, color, text_color)
        self.color = color
        self.text_color = text_color

        self.x = tk.StringVar()
        self.y = tk.StringVar()


        self.points = []

        self.coord_frame = tk.Frame(self)
        self.btns_frame = tk.Frame(self)

        self.labels_frame = tk.Frame(self.coord_frame)


        self.entries_frame = tk.Frame(self.coord_frame)
        self.point_x = tk.Entry(self.entries_frame, textvariable=self.x)
        self.point_y = tk.Entry(self.entries_frame, textvariable=self.y)

        self.upper_btns_frame = tk.Frame(self.btns_frame)

        self.btn_add_point = tk.Button(self.upper_btns_frame, text = 'Добавить точку')
        self.btn_connect_figure = tk.Button(self.upper_btns_frame, text='Замкнуть фигуру')
        self.btn_add_seed_point = tk.Button(self.btns_frame, text='Добавить затравочную точку')

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

        self.upper_btns_frame.config(bg=self.color)
        self.upper_btns_frame.pack(fill='both', expand=False, side='top')



    def coordinates_interface(self):
        self.labels_frame.config(bg=self.color)
        self.labels_frame.pack(fill='both', expand=False, side='top')

        label_x = tk.Label(self.labels_frame, text = 'X:', bg=self.color, font = Font, fg = 'white')
        label_x.pack(side = 'left', expand = True)
        label_y = tk.Label(self.labels_frame, text='Y:', bg=self.color, font = Font, fg = 'white')
        label_y.pack(side = 'left', expand = True)

        self.entries_frame.config(bg=self.color)
        self.entries_frame.pack(fill='both', expand=False, side='top')

        self.point_x.pack(side='left', expand=True)
        self.point_y.pack(side='left', expand=True)


    def btns_interface(self):
        self.btn_add_point.config(bg = self.color, font = Font, fg = self.text_color)
        self.btn_add_point.pack(fill='both', expand=True, side = 'left')
        self.btn_connect_figure.config(bg=self.color, font=Font, fg=self.text_color)
        self.btn_connect_figure.pack(fill='both', expand=True, side='left')

        self.btn_add_seed_point.config(bg=self.color, font=Font, fg=self.text_color)
        self.btn_add_seed_point.pack(fill='both', expand=True, side='bottom')



    def get_coordinate(self):
        return (self.x.get(), self.y.get())

    def add_point(self):
        pair = self.get_coordinate()
        if pair == 0:
            return
        x, y = pair
        self.points.append((x, y))
        self.points_list_box.insert(tk.END, "{:3d}) X = {:4d}; Y = {:4d}".format(len(self.points), int(x), int(y)))



class EllipsFrame(OptionFrame):
    def __init__(self, parent_frame, name = 'Option', color = 'darkslategray', text_color = 'white'):
        super().__init__(parent_frame, name, color, text_color)
        self.color = color
        self.text_color = text_color

        self.x = tk.StringVar()
        self.y = tk.StringVar()
        self.radius = tk.StringVar()
        self.a = tk.StringVar()
        self.b = tk.StringVar()

        self.center_frame = tk.Frame(self)
        self.circle_frame = tk.Frame(self)
        self.ellipse_frame = tk.Frame(self)

        self.center_x = tk.Entry(self.center_frame, textvariable= self.x)
        self.center_y = tk.Entry(self.center_frame, textvariable= self.y)

        self.radius_frame = tk.Frame(self.circle_frame)
        self.radius_entry = tk.Entry(self.radius_frame, textvariable= self.radius)

        self.a_frame = tk.Frame(self.ellipse_frame)
        self.b_frame = tk.Frame(self.ellipse_frame)
        self.a_coeff = tk.Entry(self.a_frame, textvariable= self.a)
        self.b_coeff = tk.Entry(self.b_frame, textvariable= self.b)

        self.btn_circles = tk.Button(self.circle_frame, text='Окружность')
        self.btn_ellipses = tk.Button(self.ellipse_frame, text='Эллипс')

        self.all_interface()

    def all_interface(self):
        self.pack_interface()
        #self.center_interface()

        self.circle_input_interface()
        self.ellipse_input_interface()



    def pack_interface(self):
        self.center_frame.config(bg = self.color)
        self.center_frame.pack(fill = 'both', expand=False, side='top')

        self.circle_frame.config(bg= self.color, relief="groove", borderwidth=2)
        self.circle_frame.pack( fill = 'both', expand=True, side='left')

        self.ellipse_frame.config(bg= self.color, relief="groove", borderwidth=2)
        self.ellipse_frame.pack(fill = 'both', expand= True, side='left')

        self.radius_frame.config(bg= self.color)
        self.radius_frame.pack(fill='both', expand=False, side='top')

        self.a_frame.config(bg=self.color)
        self.a_frame.pack(fill='both', expand=False, side='top')
        self.b_frame.config(bg=self.color)
        self.b_frame.pack(fill='both', expand=False, side='top')


    def circle_input_interface(self):
        self.btn_circles.pack(side='bottom', padx=10, pady=5, fill="x")
        radius_label = tk.Label(self.radius_frame, text='Радиус:')
        radius_label.pack(side='left', padx=10, pady=5, fill="x")
        self.radius_entry.pack(side='left', padx=10, pady=5)

        for i in [self.btn_circles, radius_label]:
            i.config(bg = self.color, fg = self.text_color, font = Font)


    def ellipse_input_interface(self):

        acoeff_label = tk.Label(self.a_frame, text='A:')
        acoeff_label.pack(side='left', padx=10, pady=5, fill="x")
        self.a_coeff.pack(side='left', padx=10, pady=5)


        bcoeff_label = tk.Label(self.b_frame, text='B:')
        bcoeff_label.pack(side='left', padx=10, pady=5, fill="x")
        self.b_coeff.pack(side='left', padx=10, pady=5)

        self.btn_ellipses.pack(side='top', padx=10, pady=5, fill="x")

        for i in [self.btn_ellipses, acoeff_label, bcoeff_label]:
            i.config(bg = self.color, fg = self.text_color, font = Font)

    #
    def get_center(self):
        x = self.x.get()
        y = self.y.get()
        try:
            x = int(x)
            y = int(y)
        except Exception:
            messagebox.showwarning("Ошибка",
                                   "Неверно заданы координаты центра!\n"
                                   "Ожидался ввод целых чисел.")
            return 0

        return (x, y)

    def get_radius(self):
        radius = self.radius.get()

        try:
            radius = int(radius)
        except Exception:
            messagebox.showwarning("Ошибка",
                                   "Неверно задан радиус окружности!\n"
                                   "Ожидался ввод целых чисел.")
            return 0
        if (radius <= 0):
            messagebox.showwarning("Ошибка",
                                   "Неверно задан радиус окружности!\n"
                                   "Радиус не может быть меньше 1.")
            return 0
        return radius

    def get_ellipse_parameters(self):
        a = self.a.get()
        b = self.b.get()
        try:
            a = int(a)
            b = int(b)
            if a <= 0 or b <= 0:
                messagebox.showwarning("Ошибка",
                                       "Неверно заданы радиусы A и B эллипса!\nA и B не могут быть меньше 1.\n")
                return 0
        except Exception:
            messagebox.showwarning("Ошибка",
                                   "Неверно заданы радиусы A и B эллипса!\n"
                                   "Ожидался ввод целых чисел.")
            return 0

        return (a, b)


class MouseInputFrame(OptionFrame):
    def __init__(self, parent_frame, name = 'Option', color = 'darkslategray', text_color = 'white'):
        super().__init__(parent_frame, name, color, text_color)
        self.color = color
        self.text_color = text_color

        self.btn_circle_time = tk.Label(self, text = 'Добавить точку - левая кнопка мыши')
        self.btn_ellips_time = tk.Label(self, text = 'Замкнуть фигуру - правая кнопка мыши')
        self.lbl_seed_point = tk.Label(self, text='Добавить затравочную точку - ...')

        self.analyzis_interface()

    def analyzis_interface(self):
        self.btn_circle_time.config(bg = self.color, font = Font, fg = self.text_color)
        self.btn_circle_time.pack(side = 'top', expand = True, fill = 'x')
        self.btn_ellips_time.config(bg=self.color, font=Font, fg=self.text_color)
        self.btn_ellips_time.pack(side = 'top', expand = True, fill = 'x')
        self.lbl_seed_point.config(bg=self.color, font=Font, fg=self.text_color)
        self.lbl_seed_point.pack(side='top', expand=True, fill='x')


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
        self.drawing_mode_frame = DrawingModeFrame(self, 'Режим закраски')
        self.keyboard_frame = KeyboardInputFrame(self, 'Ввод с клавиатуры: точка')
        self.ellipse_frame = EllipsFrame(self, "Ввод с клавиатуры: окружность/эллипс")
        self.mouse_frame = MouseInputFrame(self, 'Ввод мышью')
        self.time_frame = AnalyzisFrame(self, 'Измерение времени')


        self.btn_fill_figure = tk.Button(self, text='Выполнить закраску фигуры', bg='darkslategray', fg='white', font=('Arial', 20))

        self.btn_clear = tk.Button(self, text='Очистить', bg='darkslategray', fg='white', font=('Arial', 20))
        self.btn_info = tk.Button(self, text='Справка', bg = 'darkslategray', fg = 'white', font = ('Arial', 20))

        self.actions_interface()



    def actions_interface(self):
        self.btn_fill_figure.pack(fill='both', expand=False, side='top')
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





###########################
class ListFrame(MainFrame):
    def __init__(self, root, color=None):
        self.color = color
        super().__init__(root)

        self.points_list_frame = OptionFrame(self, 'Спиcок фигур')
        self.points_list_box = tk.Listbox(self.points_list_frame)
        self.points_list_interface()


    def points_list_interface(self):


        self.points_list_frame.config(bg=self.color)
        self.points_list_frame.pack(fill='y', expand=True, side='top')

        self.make_listbox_scrollable()
        self.points_list_box.pack(fill='both', expand=True, side='left')

    def make_listbox_scrollable(self):
        '''
        config Listbox to be scrollable
        '''

        vbar = tk.Scrollbar(self.points_list_frame, orient='vertical')
        vbar.pack(side='left', fill='y')
        vbar.config(command=self.points_list_box.yview)



        hbar = tk.Scrollbar(self.points_list_frame, orient='horizontal')
        hbar.pack(side='bottom', fill='x')
        hbar.config(command=self.points_list_box.xview)


        self.points_list_box.config(yscrollcommand=vbar.set)#, xscrollcommand=hbar.set)

        self.points_list_box.pack(side='left', expand=True, fill='both')



