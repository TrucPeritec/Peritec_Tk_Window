import tkinter as tk
from Peritec_Tk_Window import *

from time import sleep

class window1(Peritec_Tk_Window):
    def __init__(self, window_name, top = None, loop_period = 1, add_to_collection = True):
        Peritec_Tk_Window.__init__(self, window_name, top, loop_period, add_to_collection)

        top = self.top 

        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x450+660+210")
        top.minsize(120, 1)
        top.maxsize(3290, 1061)
        top.resizable(1,  1)
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.083, rely=0.067, height=20, relwidth=0.14)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="blue")
        self.Entry1.configure(selectforeground="white")

        self.Button1 = tk.Button(top, command = lambda: self.button1Clicked())
        self.Button1.place(relx=0.117, rely=0.178, height=24, width=47)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Button''')

        self.Entry2 = tk.Entry(top)
        self.Entry2.place(relx=0.3, rely=0.3, height=20, relwidth=0.14)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(highlightbackground="#d9d9d9")
        self.Entry2.configure(highlightcolor="black")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(selectbackground="blue")
        self.Entry2.configure(selectforeground="white")

        self.Button2 = tk.Button(top, command = lambda: self.button2Clicked())
        self.Button2.place(relx=0.5, rely=0.5, height=24, width=47)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Button''')

        self.count = 0

    def button1Clicked(self):
        if not (PeritecTkWindowExistence(self.Entry1.get())):
            top2 = window2(window_name = self.Entry1.get(), add_to_collection = True)
    def button2Clicked(self):
        PeritecTkWindowDelete(self.Entry2.get())

    def run(self):
        # print("Enqueue")
        # self.enqueue("xxx", {"sdf":"dfs", "111":23123})
        
        # sleep(0.1)

        # print("Dequeue")
        # print(self.dequeue()["data"])
        self.count = self.count + 1
        print(self.count)
        # print(len(PeritecTkWindowGetCollection()))
        
        # sleep(0.1)



class window2(Peritec_Tk_Window):
    def __init__(self, window_name, top = None, loop_period = 1, add_to_collection = True):
        Peritec_Tk_Window.__init__(self, window_name, top, loop_period, add_to_collection)

        top = self.top 

        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x450+660+210")
        top.minsize(120, 1)
        top.maxsize(3290, 1061)
        top.resizable(1,  1)
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.5, rely=0.067, height=20, relwidth=0.14)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.55, rely=0.156, height=34, width=47)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Button''')
        
        self.count = 0

    def run(self):
        pass
        # print("Enqueue")
        # self.enqueue("xxx", {"sdf":"dfs", "111":23123})
        
        # sleep(0.1)

        # print("Dequeue")
        # print(self.dequeue()["data"])
        # print(len(PeritecTkWindowGetCollection()))
        
        # sleep(0.5)
        self.count = self.count + 1
        print(str(self.count) + "---")





root = tk.Tk()
window1("main", root)
root.mainloop()