
import tkinter as tk
import tkinter.messagebox as box


class Main_Frame(tk.Frame):
    def __init__(self, root, color):
        super().__init__(root)
        self.color = color
        self.interface()

    def interface(self):
        self.pack(fill='both', expand=True, side='left')
        self.config(bg = self.color)

        #actions_frame = tk.Frame(self, relief="raised", borderwidth=1) #- это в init как-то можно прописать при желании
        #actions_frame.config(bg=self.color)
        #actions_frame.pack(fill='both', expand = True, side= 'left' )
        #self.pack(fill='both', expand=True, side='left')




class Cnvs_Frame(Main_Frame):
    def __init__(self, root, color):
        super().__init__(root, color)
        #self.canva = tk.Canvas(self)
        self.interface()

    def interface(self):
        canva = tk.Canvas(self)
        canva.pack(fill='both', expand = True)
