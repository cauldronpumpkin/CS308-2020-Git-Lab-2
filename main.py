import string
from tkinter import *
from tkinter import ttk
from tkinter import filedialog, messagebox
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk) 
from split_store import *

num_of_lines, num_of_sentences, num_of_words = 0, 0, 0
def process_data(path):
    try:
        global num_of_lines, num_of_sentences, num_of_words
        (file, num_of_lines) = file_open(path)
        (lists, num_of_sentences) = list_of_sentences(file)
        (dict, num_of_words) =  split_and_store(lists)
        sorted_dict = {k: v for k, v in sorted(dict.items(), key=lambda item: item[1])}
        summarise(sorted_dict)
    except:
        return

def summarise(sorted_dict):
    global num_of_lines, num_of_sentences, num_of_words
    
    window = Toplevel()
    window.geometry("300x200")
    window.title("Summary of the text file")

    mylist = Listbox(window, width=20, height=10)
    mylist.pack(padx=10, pady=10, fill="both", expand=True)

    mylist.insert(END, "Number of lines: {}".format(num_of_lines))
    mylist.insert(END, "Number of sentences: {}".format(num_of_sentences))
    mylist.insert(END, "Number of words: {}".format(num_of_words))

    root.protocol("WM_DELETE_WINDOW", plot(list(sorted_dict.keys()), list(sorted_dict.values())))

    window.mainloop()

def plot(X, Y): 
    plot_window = Toplevel()
    plot_window.geometry("1900x1000")
    plot_window.title("Plot for words")

    fig = Figure(figsize = (19, 10), dpi = 100) 

    plot1 = fig.add_subplot(212)
    plot2 = fig.add_subplot(211)

    plot1.bar(X[:100], Y[:100],align='edge', width=0.5)
    plot1.set_title("Least occuring words")
    for tick in plot1.get_xticklabels():
        tick.set_rotation(90)
    
    plot2.bar(X[-100:], Y[-100:],align='edge', width=0.5)
    plot2.set_title("Most occuring words")
    for tick in plot2.get_xticklabels():
        tick.set_rotation(90)
    
    fig.tight_layout()
  
    canvas = FigureCanvasTkAgg(fig, master = plot_window)   
    canvas.draw() 
   
    canvas.get_tk_widget().pack() 
  
    toolbar = NavigationToolbar2Tk(canvas, plot_window) 
    toolbar.update() 

    canvas.get_tk_widget().pack()
    plot_window.mainloop() 

def print_keyword_sentences(sent):
    window = Toplevel()
    window.geometry("500x500")
    window.title("Sentences found after keyword search")

    scrollbar = Scrollbar(window, orient="vertical")
    scrollbar.pack( side = "right", fill = "y" )

    mylist = Listbox(window, width=20, height=10, yscrollcommand = scrollbar.set)
    mylist.pack(padx=10, pady=10, fill="both", expand=True)
    for line in sent:
        mylist.insert(END, str(line))

    window.mainloop() 

def keyword_search():
    try:
        file = open(filepath.get(), 'r').read().splitlines()
        lists,_ = list_of_sentences(file)
        sets = get_keyword_set(keywordpath.get())
        key_sentences = get_keyword_sentences(lists,sets)
        print_keyword_sentences(key_sentences)
    except:
        return

def refresh():
    if (filepath.get() == ""):
        messagebox.showerror("No File Found", "Please pick a file first.")  
        return
    else:
        process_data(filepath.get())

def clear():
    filepath.set("")
    filename.set("")
    keywordpath.set("")
    keywordname.set("")
    dynamic_button['text'] = "Pick File"
    dynamic_button['command'] = pick_file
    dynamic_keyword_button['text'] = "Pick Keyword file"
    dynamic_keyword_button['command'] = pick_keyword_file


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
