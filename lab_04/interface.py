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
        label_name.pack(expand = True, fill = 'x')
        self.pack(fill='both', expand=True, side='top')
        if self.color:
            self.config(bg=self.color)
        self.config(highlightbackground="black", highlightthickness=1)


class AlgorithmFrame(OptionFrame):
    def __init__(self, parent_frame, name = 'Option', color = 'darkslategray', text_color = 'white'):
        super().__init__(parent_frame, name, color, text_color)
        self.color = color
        self.text_color = text_color

        self.ALGOS = [('Каноническое уравнение', '1'), ('Параметрическое уравнение', '2'), ('Брезенхэма', '3'),
                      ('Средней точки', '4'), ('Библиотечный', '5')]

        self.alg_frame1 = tk.Frame(self, bg = self.color)
        self.alg_frame1.pack(side = 'left', expand = True)
        self.alg_frame2 = tk.Frame(self, bg = self.color)
        self.alg_frame2.pack(side='left', expand=True)

        self.algorithm = tk.StringVar() # какой алгоритм выбран
        self.algorithm.set("5")
        self.algorithms = self.create_algorithms()#[self.create_radio(c) for c in self.ALGOS]

        self.algorithm_interface()

    def create_radio(self, option, frame):
        text, value = option
        return tk.Radiobutton(frame, bg = self.color, selectcolor = self.color,
                              text=text, value=value, variable=self.algorithm, font = Font, fg = 'white')

    def create_algorithms(self):
        algos = []
        for i in range( len(self.ALGOS) // 2):
            algos.append( self.create_radio(self.ALGOS[i], self.alg_frame1) )

        for i in range(len(self.ALGOS) // 2, len(self.ALGOS)):
            algos.append( self.create_radio(self.ALGOS[i], self.alg_frame2) )
        return algos

    def algorithm_interface(self):
        for button in self.algorithms:
            button.pack(anchor=tk.W, padx=10, pady=5)
            button.config(font = Font)

    def get_algorithm(self):
        return self.algorithm.get()


class ColorFrame(OptionFrame):
    def __init__(self, parent_frame, name = 'Option',
             color = 'darkslategray', text_color = 'white'):

        super().__init__(parent_frame, name, color, text_color)
        self.color = color
        self.text_color = text_color

        self.line_color = 'black'

        self.chng_screen = tk.Button(self, text = 'Изменить цвет экрана', bg=self.color,
                                     font=Font, fg= text_color)

        self.color_line_frame = tk.Frame(self, bg = self.color)
        self.chng_line = tk.Button(self.color_line_frame, text = 'Изменить цвет линии', bg=self.color,
                                   font=Font, fg= text_color)
        self.line_label = tk.Label(self.color_line_frame, bg=self.color, text="Текущий цвет линии:",
                                   fg=text_color,   font=Font)
        self.cur_line_color_label = tk.Label(self.color_line_frame, bg="black")

        self.color_interface()

    def color_interface(self):
        self.chng_screen.pack(side = 'left', padx = 10, pady = 5)
        self.color_line_frame.pack(side = 'right', padx = 10, pady = 5, expand = True)
        self.chng_line.pack(side = 'top', padx=10, pady=5)
        self.line_label.pack(side = 'left', padx=10, pady=5)
        self.cur_line_color_label.pack(side = 'left', padx=10, pady=5, fill = 'x', expand = 'true')

    def set_line_color(self, color):
        self.line_color = color


    def get_line_color(self):
        return self.line_color


    '''
    def set_functions(self, functions_array):
        buttons = [self.chng_screen, self.chng_line]
        butns_and_func = [(x,y) for x,y in zip(buttons, functions_array)]

        for btn in butns_and_func:
            btn[0].config(command = btn[1])
    '''


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
        self.center_interface()

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



    def center_interface(self):
        label_center = tk.Label(self.center_frame, text='Координаты центра:')
        label_center.pack(side='top', padx=10, pady=5, fill="x")

        label_x = tk.Label(self.center_frame, text='X:')
        label_x.pack(side='left', padx=10, pady=5, fill="x")
        self.center_x.pack(side='left', padx=10, pady=5)

        self.center_y.pack(side='right', padx=10, pady=5)
        label_y = tk.Label(self.center_frame, text='Y:')
        label_y.pack(side='right', padx=10, pady=5, fill="x")

        for i in [label_center, label_x, label_y]:
            i.config(bg = self.color, fg = self.text_color, font = Font)


    def circle_input_interface(self):
        self.btn_circles.pack(side='bottom', padx=10, pady=5, fill="x")
        radius_label = tk.Label(self.radius_frame, text='Радиус:')
        radius_label.pack(side='left', padx=10, pady=5, fill="x")
        self.radius_entry.pack(side='left', padx=10, pady=5)

        for i in [self.btn_circles, radius_label]:
            i.config(bg = self.color, fg = self.text_color, font = Font)


    def ellipse_input_interface(self):

        acoeff_label = tk.Label(self.a_frame, text='a:')
        acoeff_label.pack(side='left', padx=10, pady=5, fill="x")
        self.a_coeff.pack(side='left', padx=10, pady=5)


        bcoeff_label = tk.Label(self.b_frame, text='b:')
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


class SpectrumFrame(OptionFrame):
    def __init__(self, parent_frame, name = 'Option', color = 'darkslategray', text_color = 'white'):
        super().__init__(parent_frame, name, color, text_color)
        self.color = color
        self.text_color = text_color

        self.steps = tk.StringVar()
        self.fig_num = tk.StringVar()
        self.start_radius =  tk.StringVar()
        self.start_a_coeff = tk.StringVar()
        self.start_b_coeff = tk.StringVar()

        self.common_frame = tk.Frame(self)
        self.difference_frame = tk.Frame(self)

        self.step_frame = tk.Frame(self.common_frame)
        self.num_frame = tk.Frame(self.common_frame)

        self.circle_frame = tk.Frame(self.difference_frame)
        self.ellipse_frame = tk.Frame(self.difference_frame)


        self.btn_circles = tk.Button(self.circle_frame, text='Спектр окружностей')
        self.btn_ellipses = tk.Button(self.ellipse_frame, text='Спектр эллипсов')

        self.radius_frame = tk.Frame(self.circle_frame)


        self.raduis = tk.Entry(self.radius_frame, textvariable= self.start_radius)
        self.a_frame = tk.Frame(self.ellipse_frame)
        self.b_frame = tk.Frame(self.ellipse_frame)

        self.a_coeff_entry = tk.Entry(self.a_frame, textvariable= self.start_a_coeff)
        self.b_coeff_entry = tk.Entry(self.b_frame, textvariable= self.start_b_coeff)
        self.figure_number = tk.Entry(self.num_frame, textvariable= self.fig_num)
        self.step = tk.Entry(self.step_frame, textvariable= self.steps)

        self.spectrum_interface()

    def spectrum_interface(self):
        self.pack_frames_interface()
        self.common_interface()

        self.circle_input_interface()
        self.ellipse_input_interface()


    def pack_frames_interface(self):
        self.common_frame.config(bg=self.color)
        self.common_frame.pack(fill='both', expand=False, side='top')

        self.difference_frame.config(bg=self.color)
        self.difference_frame.pack(fill='both', expand=False, side='top')

        self.step_frame.config(bg=self.color)
        self.step_frame.pack(fill='both', expand=False, side='left')
        self.num_frame.config(bg=self.color)
        self.num_frame.pack(fill='both', expand=False, side='left')

        self.circle_frame.config(bg=self.color, relief="groove", borderwidth=2)
        self.circle_frame.pack(fill='both', expand=False, side='left')

        self.radius_frame.config(bg=self.color)
        self.radius_frame.pack(fill='both', expand=False, side='top')

        self.ellipse_frame.config(bg=self.color, relief="groove", borderwidth=2)
        self.ellipse_frame.pack(fill='both', expand=False, side='right')

        self.a_frame.config(bg=self.color)
        self.a_frame.pack(fill='both', expand=False, side='top')
        self.b_frame.config(bg=self.color)
        self.b_frame.pack(fill='both', expand=False, side='top')



    def common_interface(self):
        label_step = tk.Label(self.step_frame, text='Шаг:')
        label_step.pack(side='left', padx=10, pady=5, fill="x")
        self.step.pack(side='left', padx=10, pady=5)

        label_num = tk.Label(self.num_frame, text='Количество фигур:')
        label_num.pack(side='left', padx=10, pady=5, fill="x")
        self.figure_number.pack(side='left', padx=10, pady=5)

        for i in [label_step, label_num]:
            i.config(bg = self.color, fg = self.text_color, font = Font)


    def circle_input_interface(self):
        radius_label = tk.Label(self.radius_frame, text='Начальный радиус:')
        radius_label.pack(side='left', padx=10, pady=5, fill="x")
        self.raduis.pack(side='left', padx=10, pady=5)

        self.btn_circles.pack(side='bottom', padx=10, pady=5, fill="y")

        for i in [radius_label, self.btn_circles]:
            i.config(bg = self.color, fg = self.text_color, font = Font)

    def ellipse_input_interface(self):

        acoeff_label = tk.Label(self.a_frame, text='Начальный А:')
        acoeff_label.pack(side='left', padx=10, pady=5, fill="x")
        self.a_coeff_entry.pack(side='left', padx=10, pady=5)


        bcoeff_label = tk.Label(self.b_frame, text='Начальный B:')
        bcoeff_label.pack(side='left', padx=10, pady=5, fill="x")
        self.b_coeff_entry.pack(side='left', padx=10, pady=5)

        self.btn_ellipses.pack(fill='both', expand=True, side='top')

        for i in [acoeff_label, bcoeff_label, self.btn_ellipses]:
            i.config(bg = self.color, fg = self.text_color, font = Font)


    #
    def get_start_radius(self):
        radius = self.start_radius.get()

        try:
            radius = int(radius)
        except Exception:
            messagebox.showwarning("Ошибка",
                                   "Неверно задан начальный радиус окружности!\n"
                                  "Ожидался ввод целых чисел.")
            return 0
        if (radius <= 0):
            messagebox.showwarning("Ошибка",
                                   "Неверно задан радиус окружности!\n"
                                   "Радиус не может быть меньше 1.")
            return 0
        return radius

    def get_start_ellipse_parameters(self):
        a = self.start_a_coeff.get()
        b = self.start_b_coeff.get()
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

        return(a, b)


    def get_step(self):
        step_ret = self.steps.get()

        try:
            step_ret = int(step_ret)
        except Exception:
            messagebox.showwarning("Ошибка",
                                   "Неверно задан шаг спектра!\n"
                                   "Ожидался ввод целого числа.")
            return 0
        if (step_ret <= 0):
            messagebox.showwarning("Ошибка",
                                   "Неверно задан шаг спектра!\n"
                                   "Шаг не может быть меньше 1.")
            return 0
        return step_ret

    def get_number_figures(self):
        num_fig = self.fig_num.get()

        try:
            num_fig = int(num_fig)
        except Exception:
            messagebox.showwarning("Ошибка",
                                   "Неверно задано количество фигур!\n"
                                   "Ожидался ввод целого числа.")
            return 0
        if (num_fig <= 0):
            messagebox.showwarning("Ошибка",
                                   "Неверно задано количество фигур!\n"
                                   "Их количество не может быть меньше 1.")
            return 0
        return num_fig




class AnalyzisFrame(OptionFrame):
    def __init__(self, parent_frame, name = 'Option', color = 'darkslategray', text_color = 'white'):
        super().__init__(parent_frame, name, color, text_color)
        self.color = color
        self.text_color = text_color

        self.btn_circle_time = tk.Button(self, text = 'Окружность')
        self.btn_ellips_time = tk.Button(self, text = 'Эллипс')

        self.analyzis_interface()

    def analyzis_interface(self):
        self.btn_circle_time.config(bg = self.color, font = Font, fg = self.text_color)
        self.btn_circle_time.pack(side = 'left', expand = True, fill = 'x')
        self.btn_ellips_time.config(bg=self.color, font=Font, fg=self.text_color)
        self.btn_ellips_time.pack(side = 'left', expand = True, fill = 'x')

##################################################################################################

class ActionsFrame(MainFrame):
    def __init__(self, root, color=None):
        self.color = color
        super().__init__(root)


        self.color_frame = ColorFrame(self, 'Цвета')
        self.ellips_frame = EllipsFrame(self, 'Задание окружности/эллипса')
        self.spectrum_frame = SpectrumFrame(self, 'Задание спектра окружностей/эллипсов')
        self.algos_frame = AlgorithmFrame(self, 'Алгоритмы построения')
        self.analyzis_frame = AnalyzisFrame(self, 'Сравнение времени алгоритмов')

        self.btn_clear = tk.Button(self, text='Очистить', bg='darkslategray', fg='white', font=('Arial', 20))
        self.btn_info = tk.Button(self, text='Справка', bg = 'darkslategray', fg = 'white', font = ('Arial', 20))

        self.actions_interface()



    def actions_interface(self):

        #self.color_frame.pack()
        #self.ellips_frame.pack()
        #self.spectrum_frame.pack()
        #self.algos_frame.pack()
        #self.analyzis_frame.pack()

        self.btn_clear.pack(fill='both', expand=False, side='top')
        self.btn_info.pack(fill='both', expand=False, side='top')

    def print_info(self):
        messagebox.showinfo('Справка',
                            'С помощью данной программы можно построить окружность или эллипс 5-ми способами:\n'
                            '1) используя Каноническое уравнение;\n'
                            '2) используя Параметрическое уравнение;\n'
                            '3) Алгоритм средней точки;\n'
                            '4) Алгоритм Брезенхема;\n'
                            '5) стандартым методом.\n'
                            '\nДля построения окружности необходимо задать центр (Xc, Yc)\n'
                            'и радиус R и выбрать метод построения из списка предложенных.\n'
                            '\nДля построения эллипса необходимо задать центр (Xc, Yc)\n'
                            'и радиусы Rx и Ry; выбрать метод построения из списка предложенных.\n'
                            '\nДля построения спектра фигур\n'
                            'необходимо задать центр фигуры, радиус(ы)\n'
                            'выбрать метод для построения,\n'
                            'а также шаг изменения и количество фигур.\n'
                            '\nДля анализа времени работы построения окружности нужно нажать на кнопку "Сравнение времени построение окружности".\n'
                            '\nДля анализа времени работы построения эллипса нужно нажать на кнопку "Сравнение времени построение эллипса".\n'
                     "\nАвтор: Амбарцумова Екатерина, ИУ7-45Б\n"
                            )

    def clear_drawing(self):
        self.drawing_field.redraw_canva()





