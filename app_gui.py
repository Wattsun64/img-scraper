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
        Label(self.m, text="URL").grid(row=0, sticky=W)
        Label(self.m, text="Path").grid(row=1, sticky=W)
        Label(self.m, text="Selector").grid(row=2, sticky=W)

        self.e1 = Entry(self.m, width=26)
        self.e2 = Entry(self.m, width=26)
        self.e3 = Entry(self.m, width=10)

        self.e1.grid(row=0, column=1, columnspan=3, sticky=W)
        self.e2.grid(row=1, column=1, columnspan=3, sticky=W)
        self.e3.grid(row=2, column=1, sticky=W)

    def create_button(self):
        btn1 = Button(self.m, text="Download", command=self.button_press)
        btn2 = Button(self.m, text="Quit", command=self.stop_program)

        btn1.grid(row=2, column=2, sticky=W)
        btn2.grid(row=2, column=3, sticky=W)

    def clear_entries(self):
        self.e1.delete(0, "end")
        self.e2.delete(0, "end")
        
    def button_press(self):
        s = Web_Scraper()

        url = self.e1.get()
        path = self.e2.get()
        sel = self.e3.get()

        s.download_img(url, path)

        self.clear_entries()
