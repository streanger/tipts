#!/usr/bin/python3
import tkinter as tk
from write_file import write_file
from read_file import read_file
from get_time import full_date
from termcolor import colored
#colors: ["grey", "red", "green", "yellow", "blue", "magenta", "cyan", "white"]
import re

class Application(tk.Frame):
    def __init__(self, master=None, diaryName="DIARY.txt"):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        self.name = diaryName

    def create_widgets(self):
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")

        self.save = tk.Button(self)
        self.save["text"] = "Save data..."
        self.save["fg"] = "green"
        self.save["command"] = self.save_data
        self.save.pack(side="top")

        self.read = tk.Button(self)
        self.read["text"] = "Read post..."
        self.read["fg"] = "green"
        self.read["command"] = self.get_post_by_date
        self.read.pack(side="top")

        self.scroll = tk.Scrollbar(self)    #self instead of root - it matters
        self.text = tk.Text(self, height=20, width=50)
        self.scroll.pack(side="right", fill=tk.Y)
        self.text.pack()
        self.scroll.config(command=self.text.yview)
        self.text.config(yscrollcommand=self.scroll.set)

    def save_data(self):
        content = self.text.get("1.0", tk.END)
        if not content.split():
            return False
        #now = colored(full_date(), "cyan")  #change color during seasons??
        now = full_date()   #think about: only time if multiple posts one day
        write_file(self.name, "\n"+now, response=False)
        write_file(self.name, content, response=False)
        self.text.delete("1.0", tk.END) #clear all data in text box
        return True

    def get_post_by_date(self):
        content = self.text.get("1.0", tk.END)
        dateFormat = re.compile(r"\d\d\d\d.\d\d.\d\d")
        try:
            result = dateFormat.search(content).group()
        except:
            result = "xxxx.xx.xx"
        #print("date in text box:", result)

        diaryContent = "".join(read_file(self.name, False))
        try:
            datesIn = dateFormat.findall(diaryContent)
        except:
            datesIn = []
        datesIn = list(set(datesIn))    #remove duplicates
        datesIn.sort()
        startPoint = len(diaryContent)
        stopPoint = len(diaryContent)
        #print("result:", result)
        if result in datesIn:
            startPoint = diaryContent.find(result)
            if not datesIn[-1] == result:
                nextDate = datesIn[datesIn.index(result)+1]    #if no duplicates and sorted it should be greater than result
                stopPoint = diaryContent.find(nextDate)   #-6 if colored
            chosenDay = diaryContent[startPoint:stopPoint]    #-6 if colored
            #print(chosenDay)
            self.text.delete("1.0", tk.END)
            self.text.insert("1.0", chosenDay)
        else:
            #print("No such date. These are availabe:\n", ", ".join(datesIn))
            textData = "Available dates:\n" + ", ".join(datesIn) + "\n"
            self.text.delete("1.0", tk.END)
            self.text.insert("1.0", textData)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('{}x{}'.format(400, 350))
    root.resizable(width=False, height=False)
    root.wm_title("diary app by stranger")
    app = Application(master=root, diaryName="DIARY.txt")
    app.mainloop()
