
import tkinter as tk
import interface as inter
import tkinter.messagebox as box

WIDTH = 1000
HEIGHT = 800

if __name__ == '__main__':
    # здесь создаем окно - родительский класс, от которого будут наследовать признаки фреймы и еще что-то, возможно
    main_window = tk.Tk()
    main_window.geometry("{}x{}+1+5".format(WIDTH, HEIGHT))

    main_window.minsize(WIDTH * 3 // 4, HEIGHT * 3 // 4)
    main_window.maxsize(WIDTH * 3//2, HEIGHT*3//2)

    #Создадим меню
    MainMenu = tk.Menu(main_window)

    actions = inter.Main_Frame(main_window, 'red')
    #dd = inter.Main_Frame(main_window, 'blue')
    draw = inter.Cnvs_Frame(main_window, 'white')


    main_window.title("ЛР3")
    main_window.mainloop()

"""
from tkinter import Tk, RIGHT, BOTH, RAISED
from tkinter.ttk import Frame, Button, Style


class Example(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("Кнопки в kinter")
        self.style = Style()
        self.style.theme_use("default")

        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH, expand=True)

        self.pack(fill=BOTH, expand=True)

        closeButton = Button(self, text="Закрыть")
        closeButton.pack(side=RIGHT, padx=5, pady=5)
        okButton = Button(self, text="Готово")
        okButton.pack(side=RIGHT)


def main():
    root = Tk()
    root.geometry("300x200+300+300")
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()

"""