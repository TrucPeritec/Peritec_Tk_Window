from Peritec_Python_Thread import PeritecThreadQueue
import tkinter as tk


Peritec_tk_window_collection = {}

def PeritecTkWindowAdd(window_name, Peritec_tk_window):
    Peritec_tk_window_collection[window_name] = Peritec_tk_window

def PeritecTkWindowExistence(window_name):
    return window_name in Peritec_tk_window_collection.keys()

def PeritecTkWindowQuery(window_name):
    return Peritec_tk_window_collection[window_name]

def PeritecTkWindowGetCollection():
    return Peritec_tk_window_collection

def PeritecTkWindowDelete(window_name):
    if window_name in Peritec_tk_window_collection:
        PeritecTkWindowQuery(window_name).top.destroy()
        Peritec_tk_window_collection.pop(window_name)



class Peritec_Tk_Window(PeritecThreadQueue):
    def __init__(self, window_name, top = None, loop_period = 1, add_to_collection = True):
        PeritecThreadQueue.__init__(self)
        
        if(top == None):
            top = tk.Toplevel()
        self.top = top
        
        self.window_name = window_name
        if add_to_collection:
            PeritecTkWindowAdd(self.window_name, self)

        self.top.protocol("WM_DELETE_WINDOW", lambda: PeritecTkWindowDelete(self.window_name))

        self.loop_period = loop_period
        self.top.after(self.loop_period, lambda: self.loop())

        # UI setting up - begin ----------------------------------------

        # UI setting up - end ----------------------------------------

    def loop(self):
        self.run()
        self.top.after(self.loop_period, lambda: self.loop())
