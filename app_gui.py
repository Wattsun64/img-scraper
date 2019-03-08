from tkinter import *
from scraper_class import *

class Build_GUI:
    def __init__(self):
        self.m = Tk()

    def start_program(self):
        mainloop()

    def create_inputs(self):
        Label(self.m, text="URL").grid(row=0)
        Label(self.m, text="Path").grid(row=1)

        self.e1 = Entry(self.m)
        self.e2 = Entry(self.m)

        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)

    def create_button(self, txt="Press"):
        btn = Button(self.m, text=txt, command=self.button_press)

        btn.grid(row=3)

    def button_press(self):
        print(self.e2.get())

        self.e2.delete(0, "end")

        return True   
