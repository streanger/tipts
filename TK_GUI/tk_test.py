#!/usr/bin/python3
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")

        self.calc = tk.Button(self)
        self.calc["text"] = "Press to calc"
        self.calc["command"] = self.calculate
        self.calc.pack(side="top")

        #fm = Frame(master)

        self.label1 = tk.Label(self)
        self.label1["text"] = "LABEL1"
        self.label1.pack(side="top")
        self.entry1 = tk.Entry(self)
        self.entry1.pack(side="top")

        self.label2 = tk.Label(self)
        self.label2["text"] = "LABEL2"
        self.label2.pack(padx=5, pady=10, side="left", anchor="w")
        self.entry2 = tk.Entry(self)
        self.entry2.pack(padx=5, pady=10, side="left", anchor="w")


    def say_hi(self):
        print("hi there, everyone!")

    def calculate(self):
        text = self.entry1.get()
        print(text)


root = tk.Tk()
root.geometry('{}x{}'.format(400, 300))
root.resizable(width=False, height=False)
app = Application(master=root)
app.mainloop()
