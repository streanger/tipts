import ctypes
import tkinter as tk

def filled_widget():
    root = tk.Tk()
    root.geometry('{}x{}'.format(600, 500))
    root.resizable(width=False, height=False)
    root.title("gui app")
    tk.Button(text="this is very filled button").pack(expand=tk.YES, fill=tk.BOTH)
    tk.Button(text="other one").pack(expand=tk.YES, fill=tk.BOTH)
    tk.mainloop()

if __name__ == "__main__":
    #tip from: https://sciter.com/forums/topic/hide-python-consol/
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
    filled_widget()