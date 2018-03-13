#!/usr/bin/python3
import tkinter as tk
from write_file import write_file
from get_time import full_date
from termcolor import colored
#colors: ["grey", "red", "green", "yellow", "blue", "magenta", "cyan", "white"]

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")

        self.save = tk.Button(self)
        self.save["text"] = "Save data..."
        self.save["fg"] = "green"
        self.save["command"] = self.save_data
        self.save.pack(side="top")


        self.scroll = tk.Scrollbar(self)    #self instead of root - it matters
        self.text = tk.Text(self, height=20, width=50)
        self.scroll.pack(side="right", fill=tk.Y)
        self.text.pack()
        self.scroll.config(command=self.text.yview)
        self.text.config(yscrollcommand=self.scroll.set)

    def save_data(self):
        content = self.text.get("1.0", tk.END)
        now = colored(full_date(), "cyan")  #change color during seasons??
        write_file("TEST.txt", "\n"+now, response=False)
        write_file("TEST.txt", content, response=False)
        #print(content)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('{}x{}'.format(400, 350))
    root.resizable(width=False, height=False)
    app = Application(master=root)
    app.mainloop()
