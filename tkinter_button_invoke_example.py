'''invoke button example'''
import time
from tkinter import *
from threading import Thread


def button_func():
    print('{} -> button is pressed'.format(time.strftime('%M:%S')))
    
    
def invoke_button():
    while True:
        example_button.config(relief = "sunken")
        master.update()
        time.sleep(0.25)
        example_button.invoke()
        example_button.config(relief = "raised")
        master.update()
        time.sleep(0.25)
        
        
if __name__ == "__main__":
    master = Tk()
    
    master.geometry("{}x{}+333+50".format(300, 300))
    master.resizable(width=False, height=False)
    master.wm_title("gui_app")
    
    example_button = Button(master, text='BUTTON', command=button_func)
    example_button.pack(expand=YES, fill=BOTH)
    invoke_thread = Thread(target=invoke_button)
    invoke_thread.start()
    
    master.mainloop()
    