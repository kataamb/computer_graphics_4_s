import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as box



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

        # config Canvas to be scrollable

        hbar = tk.Scrollbar(self, orient='horizontal')
        hbar.pack(side='bottom', fill='x')
        hbar.config(command=self.canva.xview)

        vbar = tk.Scrollbar(self, orient='vertical')
        vbar.pack(side='left', fill='y')
        vbar.config(command=self.canva.yview)

        self.canva.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)

        self.canva.pack(side='left', expand=True, fill='both')
        #

        self.canvas_interface()


    def canvas_interface(self):
        #self.canva.pack(fill='both', expand=True, side='left')
        self.canva.config(bg = 'white')
        self.redraw_canva()

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
        label_name = tk.Label(self, text = self.name, bg = self.color,
                              fg = self.name_color, font = ('Arial', 20))
        label_name.pack()
        self.pack(fill='both', expand=True, side='top')
        if self.color:
            self.config(bg=self.color)
        self.config(highlightbackground="black", highlightthickness=1)


class AlgorithmFrame(OptionFrame):
    def __init__(self, parent_frame, name = 'Option', color = 'darkslategray', text_color = 'white'):
        super().__init__(parent_frame, name, color, text_color)
        self.color = color
        self.text_color = text_color

        self.ALGOS = [('ЦДА', '1'), ('Брезенхэм f', '2'), ('Брезенхэм i', '3'),
                      ('Брезенхэм устр', '4'), ('By', '5'), ('Библиотечный', '6')]
        self.algorithm = tk.StringVar() # какой алгоритм выбран
        self.algorithm.set("6")
        self.algorithms = [self.create_radio(c) for c in self.ALGOS]

        self.algorithm_interface()

    def create_radio(self, option):
        text, value = option
        return tk.Radiobutton(self, bg = self.color, selectcolor = self.color,
                              text=text, value=value, variable=self.algorithm)


    def algorithm_interface(self):
        for button in self.algorithms:
            button.pack(anchor=tk.W, padx=10, pady=5)

    #--------
    #methods of class
    def get_algorithm(self):
        return self.algorithm


class ColorFrame(OptionFrame):
    def __init__(self, parent_frame, name = 'Option',
             color = 'darkslategray', text_color = 'white'):

        super().__init__(parent_frame, name, color, text_color)
        self.color = color
        self.text_color = text_color

        self.chng_screen = tk.Button(self, text = 'Change screen', bg='lightslategray',
                                     font=("Consolas", 16))
        self.chng_line = tk.Button(self, text = 'Change line', bg='lightslategray',
                                   font=("Consolas", 16))
        self.line_label = tk.Label(self, bg=self.color, text="Текущий цвет линии:",
                                   fg='white',   font=("Consolas", 16))
        self.cur_line_color_label = tk.Label(self, bg="black")

        self.color_interface()

    def color_interface(self):
        self.chng_screen.pack(anchor = tk.W, padx = 10, pady = 5)
        self.chng_line.pack(anchor=tk.W, padx=10, pady=5)
        self.line_label.pack(side = 'left', padx=10, pady=5)
        self.cur_line_color_label.pack(side = 'left', padx=10, pady=5)





    def set_functions(self, functions_array):
        buttons = [self.chng_screen, self.chng_line]
        butns_and_func = [(x,y) for x,y in zip(buttons, functions_array)]

        for btn in butns_and_func:
            btn[0].config(command = btn[1])


class EllipsFrame(OptionFrame):
    def __init__(self, parent_frame, name = 'Option', color = 'darkslategray', text_color = 'white'):
        super().__init__(parent_frame, name, color, text_color)
        self.color = color
        self.text_color = text_color

        self.ellips_interface()

    def ellips_interface(self):
        pass


class SpectrumFrame(OptionFrame):
    def __init__(self, parent_frame, name = 'Option', color = 'darkslategray', text_color = 'white'):
        super().__init__(parent_frame, name, color, text_color)
        self.color = color
        self.text_color = text_color

        self.spectrum_interface()

    def spectrum_interface(self):
        pass


class AnalyzisFrame(OptionFrame):
    def __init__(self, parent_frame, name = 'Option', color = 'darkslategray', text_color = 'white'):
        super().__init__(parent_frame, name, color, text_color)
        self.color = color
        self.text_color = text_color

        self.analyzis_interface()

    def analyzis_interface(self):
        pass

##################################################################################################

class ActionsFrame(MainFrame):
    def __init__(self, root, color=None):
        self.color = color
        super().__init__(root)

        self.algos_frame = AlgorithmFrame(self, 'Алгоритмы построения')
        self.color_frame = ColorFrame(self, 'Цвета')
        self.ellips_frame = EllipsFrame(self, 'Задание окружности/эллипса')
        self.spectrum_frame_circle = SpectrumFrame(self, 'Задание спектра окружностей')
        self.spectrum_frame_ellipse = SpectrumFrame(self, 'Задание спектра эллипсов')
        self.analyzis_frame = AnalyzisFrame(self, 'Сравнение времени алгоритмов')

        self.btn_clear = tk.Button(self, text='Очистить', bg='darkslategray', fg='white', font=('Arial', 20),
                                   command = self.clear_drawing)
        self.btn_info = tk.Button(self, text='Справка', bg = 'darkslategray', fg = 'white', font = ('Arial', 20),
                                  command = self.print_info)

        self.actions_interface()



    def actions_interface(self):
        self.algos_frame.pack()
        self.color_frame.pack()
        self.ellips_frame.pack()
        self.spectrum_frame_circle.pack()
        self.spectrum_frame_ellipse.pack()
        self.analyzis_frame.pack()

        self.btn_clear.pack(fill='both', expand=False, side='top')
        self.btn_info.pack(fill='both', expand=False, side='top')

    def print_info(self):
        box.showinfo('Справка',
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





