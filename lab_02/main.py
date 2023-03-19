"""
    Модуль запуска приложения
"""

import tkinter as tk
import tkinter.messagebox as box
import copy
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import ipywidgets

import tank
import update


matplotlib.use('TkAgg')


AUTHOR_TITLE = 'Об авторе'
AUTHOR = 'Амбарцумова Екатерина\nИУ7-45Б'


class RootWindow():
    """
        Класс главного окна
    """

    def __init__(self):
        """
            Конструктор класса
        """
        self.root = tk.Tk()
        self.root.geometry("1500x950+200+40")
        self.root.resizable(True, True)
        self.root.title("ЛР2")

    def crt_menu(self):
        """
            Создание меню
        """
        self.menu = tk.Menu(self.root, font="TkMenuFont")

        self.menu.add_command(
            label=AUTHOR_TITLE,
            command=lambda: box.showinfo(AUTHOR_TITLE, AUTHOR)
            )
        self.menu.add_command(
            label='Выход',
            command=self.root.destroy
            )

        self.root.configure(menu=self.menu)


    def crtwdg_figure_centre(self):
        """
            Создание виджетов центра фигуры
        """
        self.lblfrm_figure_centre = tk.LabelFrame(self.root)
        self.lblfrm_figure_centre.place(
            relx=0.017,
            rely=0.013,
            relheight=0.109,
            relwidth=0.25
            )
        self.lblfrm_figure_centre.configure(
            relief='sunken',
            font=('DejaVu Sans', 12),
            text="Центр фигуры"
            )

        self.lbl_figure_centre = tk.Label(self.lblfrm_figure_centre)
        self.lbl_figure_centre.place(
            relx=0.007,
            rely=0.370,
            relheight=0.5,
            relwidth=0.98,
            bordermode='ignore'
            )
        self.lbl_figure_centre.configure(
            font=update.FONT_CONFIG,
            text="X:{:7.2f}; Y:{:7.2f}".format(self.funcs[0].x_list[0],
                                               self.funcs[0].y_list[0])
            )


    def crtwdg_transfer(self):
        """
            Создание виджетов переноса
        """

        # фрейм для конструкции переноса
        self.lblfrm_transfer = tk.LabelFrame(self.root)
        self.lblfrm_transfer.place(
            relx=0.017,
            rely=0.133,
            relheight=0.157,
            relwidth=0.25
            )
        self.lblfrm_transfer.configure(
            relief='groove',
            font=('DejaVu Sans', 12),
            text='Перенос'
            )

        # надписи для переноса
        self.lbl_dx = tk.Label(self.lblfrm_transfer)
        self.lbl_dx.place(
            relx=0.007,
            rely=0.29,
            relheight=0.25,
            relwidth=0.15,
            bordermode='ignore'
            )
        self.lbl_dx.configure(
            font=('DejaVu Sans', 12),
            text="dx:"
            )

        self.lbl_dy = tk.Label(self.lblfrm_transfer)
        self.lbl_dy.place(
            relx=0.007,
            rely=0.637,
            relheight=0.25,
            relwidth=0.15,
            bordermode='ignore'
            )
        self.lbl_dy.configure(
            font=('DejaVu Sans', 12),
            text="dy:"
            )

        # текстовое поле для ввода x
        self.ent_dx = tk.Entry(self.lblfrm_transfer)
        self.ent_dx.place(
            relx=0.164,
            rely=0.29,
            relheight=0.25,
            relwidth=0.4,
            bordermode='ignore'
            )
        self.ent_dx.configure(
            background="white",
            font="TkFixedFont",
            selectbackground="blue",
            selectforeground="white"
            )

        # текстовое поле для ввода y
        self.ent_dy = tk.Entry(self.lblfrm_transfer)
        self.ent_dy.place(
            relx=0.171,
            rely=0.645,
            relheight=0.25,
            relwidth=0.4,
            bordermode='ignore'
            )
        self.ent_dy.configure(
            background="white",
            font="TkFixedFont",
            selectbackground="blue",
            selectforeground="white"
            )

        # кнопка для действия
        self.btn_transfer = tk.Button(self.lblfrm_transfer)
        self.btn_transfer.place(
            relx=0.6,
            rely=0.282,
            relheight=0.6,
            relwidth=0.37,
            bordermode='ignore'
            )
        self.btn_transfer.configure(
            activebackground="#f9f9f9",
            text="Перенести",
            command=lambda: update.move(self, TANK, TANKS)
            )


    def crtwdg_trans_centre(self):
        """
            Создание виджетов центра преобразований
        """
        self.lblfrm_centre = tk.LabelFrame(self.root)
        self.lblfrm_centre.place(
            relx=0.017,
            rely=0.308,
            relheight=0.147,
            relwidth=0.25
            )
        self.lblfrm_centre.configure(
            relief='groove',
            font=('DejaVu Sans', 12),
            text="Центр преобразований"
            )

        self.lbl_xc = tk.Label(self.lblfrm_centre)
        self.lbl_xc.place(
            relx=0.017,
            rely=0.259,
            relheight=0.3,
            relwidth=0.15,
            bordermode='ignore'
            )
        self.lbl_xc.configure(
            font=('DejaVu Sans', 12),
            text="Xc:"
            )

        self.lbl_yc = tk.Label(self.lblfrm_centre)
        self.lbl_yc.place(
            relx=0.02,
            rely=0.612,
            relheight=0.3,
            relwidth=0.15,
            bordermode='ignore'
            )
        self.lbl_yc.configure(
            activebackground="#f9f9f9",
            font=('DejaVu Sans', 12),
            text="Yc:"
            )

        self.ent_xc = tk.Entry(self.lblfrm_centre)
        self.ent_xc.place(
            relx=0.208,
            rely=0.284,
            relheight=0.25,
            relwidth=0.75,
            bordermode='ignore'
            )
        self.ent_xc.configure(
            background="white",
            font="TkFixedFont"
            )
        self.ent_xc.insert(0, "0.00")

        self.ent_yc = tk.Entry(self.lblfrm_centre)
        self.ent_yc.place(
            relx=0.208,
            rely=0.638,
            relheight=0.25,
            relwidth=0.75,
            bordermode='ignore'
            )
        self.ent_yc.configure(
            background="white",
            font="TkFixedFont",
            selectbackground="blue",
            selectforeground="white"
            )
        self.ent_yc.insert(0, "0.00")


    def crtwdg_scaling(self):
        """
            Создание виджетов масштабирования
        """
        self.lblfrm_scaling = tk.LabelFrame(self.root)
        self.lblfrm_scaling.place(
            relx=0.017,
            rely=0.472,
            relheight=0.157,
            relwidth=0.25
            )
        self.lblfrm_scaling.configure(
            relief='groove',
            font=('DejaVu Sans', 12),
            text="Масштабирование"
            )

        self.lbl_kx = tk.Label(self.lblfrm_scaling)
        self.lbl_kx.place(
            relx=0.007,
            rely=0.29,
            relheight=0.25,
            width=53,
            bordermode='ignore'
            )
        self.lbl_kx.configure(
            activebackground="#f9f9f9",
            font=('DejaVu Sans', 12),
            text="Kx:"
            )

        self.lbl_ky = tk.Label(self.lblfrm_scaling)
        self.lbl_ky.place(
            relx=0.507,
            rely=0.29,
            relheight=0.25,
            width=53,
            bordermode='ignore'
            )
        self.lbl_ky.configure(
            activebackground="#f9f9f9",
            font=('DejaVu Sans', 12),
            text="Ky:"
            )

        self.ent_kx = tk.Entry(self.lblfrm_scaling)
        self.ent_kx.place(
            relx=0.164,
            rely=0.27,
            relheight=0.25,
            relwidth=0.3,
            bordermode='ignore'
            )
        self.ent_kx.configure(
            background="white",
            font="TkFixedFont",
            selectbackground="blue",
            selectforeground="white"
            )

        self.ent_ky = tk.Entry(self.lblfrm_scaling)
        self.ent_ky.place(
            relx=0.664,
            rely=0.27,
            relheight=0.25,
            relwidth=0.3,
            bordermode='ignore'
            )
        self.ent_ky.configure(
            background="white",
            font="TkFixedFont",
            selectbackground="blue",
            selectforeground="white"
            )

        self.btn_scaling = tk.Button(self.lblfrm_scaling)
        self.btn_scaling.place(
            relx=0.025,
            rely=0.6,
            relheight=0.3,
            relwidth=0.945,
            bordermode='ignore'
            )
        self.btn_scaling.configure(
            activebackground="#f9f9f9",
            text="Масштабировать",
            command=lambda: update.scale(self, TANK, TANKS)
            )


    def crtwdg_rotate(self):
        """
            Создание виджетов поворота
        """
        self.lblfrm_rotate = tk.LabelFrame(self.root)
        self.lblfrm_rotate.place(
            relx=0.017,
            rely=0.649,
            relheight=0.157,
            relwidth=0.25
            )
        self.lblfrm_rotate.configure(
            relief='groove',
            font=('DejaVu Sans', 12),
            text="Поворот"
            )

        self.lbl_angle = tk.Label(self.lblfrm_rotate)
        self.lbl_angle.place(
            relx=0.025,
            rely=0.29,
            bordermode='ignore'
            )
        self.lbl_angle.configure(
            activebackground="#f9f9f9",
            font=('DejaVu Sans', 12),
            justify=tk.CENTER,
            text="Угол (°):"
            )

        self.ent_angle = tk.Entry(self.lblfrm_rotate)
        self.ent_angle.place(
            relx=0.32,
            rely=0.25,
            relheight=0.25,
            relwidth=0.65,
            bordermode='ignore'
            )
        self.ent_angle.configure(
            background="white",
            font="TkFixedFont",
            selectbackground="blue",
            selectforeground="white"
            )


        self.btn_rotate = tk.Button(self.lblfrm_rotate)
        self.btn_rotate.place(
            relx=0.025,
            rely=0.582,
            relheight=0.32,
            relwidth=0.95,
            bordermode='ignore'
            )
        self.btn_rotate.configure(
            activebackground="#f9f9f9",
            text="Повернуть",
            command=lambda: update.rotate(self, TANK, TANKS)
            )


    def crtwdg_edit(self):
        """
            Создание виджетов редактирования
        """
        self.btn_undo = tk.Button(self.root)
        self.btn_undo.place(
            relx=0.016,
            rely=0.819,
            relheight=0.075,
            relwidth=0.12
            )
        self.btn_undo.configure(
            text="← Назад",
            state=tk.DISABLED,
            command=lambda: update.undo(ROOT, TANK, TANKS)
            )

        self.btn_redo = tk.Button(self.root)
        self.btn_redo.place(
            relx=0.147,
            rely=0.819,
            relheight=0.075,
            relwidth=0.12
            )
        self.btn_redo.configure(
            activebackground="#f9f9f9",
            text="Вперед →",
            state=tk.DISABLED,
            command=lambda: update.redo(ROOT, TANK, TANKS)
            )

        self.btn_original = tk.Button(self.root)
        self.btn_original.place(
            relx=0.016,
            rely=0.905,
            relheight=0.075,
            relwidth=0.251
            )
        self.btn_original.configure(
            text="Исходное изображение",
            command=lambda: update.reset(ROOT, TANK, TANKS)
            )


    def create_matplotlib(self):
        """
            Создание окна matplotlib
        """
        margins = {
            "left"   : 0.050,
            "bottom" : 0.050,
            "right"  : 0.980,
            "top"    : 0.980
        }

        self.figure = plt.Figure(figsize=(8.5, 7.5))
        self.figure.subplots_adjust(**margins)
        self.subplt = self.figure.add_subplot(111)

        for func in self.funcs:
            self.subplt.plot(func.x_list, func.y_list, color='k', linewidth=2)

        self.subplt.set_xlim((-100, 100))
        self.subplt.set_ylim((-80, 80))
        self.subplt.grid(True)

        self.pltcnv = FigureCanvasTkAgg(self.figure, self.root)
        self.pltcnv.get_tk_widget().place(
            relx=0.28,
            rely=0.02,
            relheight=0.96,
            relwidth=0.70
            )
        #create scrollbar
        '''
        hbar = tk.Scrollbar(self.root, orient='horizontal')
        vbar = tk.Scrollbar(self.root, orient='vertical')

        self.pltcnv.get_tk_widget().config(bg='#FFFFFF', scrollregion=(-500, -500, 500, 500))
        self.pltcnv.get_tk_widget().config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)

        hbar.config(command=self.pltcnv.get_tk_widget().xview)
        vbar.config(command=self.pltcnv.get_tk_widget().yview)

        hbar.pack(side='bottom', fill='x')
        vbar.pack(side='right', fill='y')
        #self.pltcnv.pack(side='left', expand=True, fill='both')
        '''


        '''
        hbar = tk.Scrollbar(self.root, orient='horizontal')
        hbar.pack(side='bottom', fill='x')
        hbar.config(command=self.pltcnv.xview)
        vbar = tk.Scrollbar(self.root, orient='vertical')
        vbar.pack(side='right', fill='y')
        vbar.config(command=self.pltcnv.yview)
        #####self.pltcnv.config(width=300, height=300)
        self.pltcnv.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
        self.pltcnv.pack(side='left', expand=True, fill='both')
        '''
        '''
        self.hbar = Scrollbar(self.frame, orient=HORIZONTAL)
        self.vbar = Scrollbar(self.frame, orient=VERTICAL)

        self.canvas = FigureCanvasTkAgg(fig, master=self.frame)
        self.canvas.get_tk_widget().config(bg='#FFFFFF', scrollregion=(0, 0, 500, 500))
        self.canvas.get_tk_widget().config(width=300, height=300)
        self.canvas.get_tk_widget().config(xscrollcommand=self.hbar.set, yscrollcommand=self.vbar.set)
        self.canvas.get_tk_widget().grid(row=0, column=0, sticky=W + E + N + S)

        self.hbar.grid(row=1, column=0, sticky=W + E)
        self.hbar.config(command=self.canvas.get_tk_widget().xview)
        self.vbar.grid(row=0, column=1, sticky=N + S)
        self.vbar.config(command=self.canvas.get_tk_widget().yview)

        self.frame.config(width=100, height=100)  # this has no effect
        '''

    def create_widgets(self):
        """
            Создание виджетов окна
        """
        self.crt_menu()
        self.crtwdg_figure_centre()
        self.crtwdg_transfer()
        self.crtwdg_trans_centre()
        self.crtwdg_scaling()
        self.crtwdg_rotate()
        self.crtwdg_edit()
        self.create_matplotlib()


    def run(self):
        """
            Запуск окна
        """
        self.create_widgets()
        self.root.mainloop()


if __name__ == "__main__":
    ROOT = RootWindow()
    TANK = tank.Tank()
    ROOT.funcs = TANK.full
    TANKS = update.History(0, [copy.deepcopy(TANK)])
    ROOT.run()
