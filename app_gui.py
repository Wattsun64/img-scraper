from tkinter import *
from scraper_class import *

class Build_GUI:
    def __init__(self):
        self.m = Tk()

    def start_program(self):
        mainloop()

    def stop_program(self):
        self.m.destroy()

    def create_inputs(self):
        Label(self.m, text="URL").grid(row=0)
        Label(self.m, text="Path").grid(row=1)

        self.e1 = Entry(self.m)
        self.e2 = Entry(self.m)

        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)

    def create_button(self):
        btn1 = Button(self.m, text="Press", command=self.button_press)
        btn2 = Button(self.m, text="Quit", command=self.stop_program)

        btn1.grid(row=3)
        btn2.grid(row=3, column=1)

    def clear_entries(self):
        self.e1.delete(0, "end")
        self.e2.delete(0, "end")
        
    def button_press(self):
        s = Web_Scraper()

        s.download_img(self.e1.get(), self.e2.get())

        self.clear_entries()
