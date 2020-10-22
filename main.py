import string
from tkinter import *
from tkinter import ttk
from tkinter import filedialog, messagebox
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk) 

def clear():
    filepath.set("")
    filename.set("")
    keywordpath.set("")
    keywordname.set("")

def refresh():
    pass

def pick_file(*args):
    path =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("txt files","*.txt"),("all files","*.*")))

    if path != "":
        filepath.set(path)
        filename.set(path.split('/')[-1])
        dynamic_button['text'] = "Process Words"
        dynamic_button['command'] = refresh
    else:
        return

def pick_keyword_file():
    if (filepath.get() == ""):
        messagebox.showerror("No File Found", "Please pick a file first.")  
        return

    path =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("txt files","*.txt"),("all files","*.*")))

    if path != "":
        keywordpath.set(path)
        keywordname.set(path.split('/')[-1])
        dynamic_keyword_button['text'] = "Process Keywords"
        dynamic_keyword_button['command'] = keyword_search
    else:
        return

root = Tk()
root.title("File")

root.geometry("300x200")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

filepath = StringVar()
filename = StringVar()

keywordpath = StringVar()
keywordname = StringVar()

ttk.Label(mainframe, textvariable=filename).grid(column=1, row=1, sticky=(W, E))
ttk.Label(mainframe, textvariable=keywordname).grid(column=1, row=2, sticky=(W, E))

dynamic_button = ttk.Button(mainframe, text="Pick File", command=pick_file)
dynamic_button.grid(column=2, row=1, sticky=W)

dynamic_keyword_button = ttk.Button(mainframe, text="Pick Keyword file", command=pick_keyword_file)
dynamic_keyword_button.grid(column=2, row=2, sticky=W)

clear_button = ttk.Button(mainframe, text="Clear", command=clear)
clear_button.grid(column=2, row=3, sticky=W)

refresh_button = ttk.Button(mainframe, text="Refresh", command=refresh)
refresh_button.grid(column=2, row=4, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

root.mainloop()