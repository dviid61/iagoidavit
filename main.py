import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("APP")
        self.geometry("500x500")
        self.resizable(0, 0)
        
        self.grid_columnconfigure((0,1), uniform = "a", weight = 1)
        self.grid_rowconfigure((0,1), uniform = "a", weight = 1)
        
        mainMenu = Menu(self)
        self.config(menu = mainMenu)
        
        Frame(self)
        
        self.mainloop()


class Menu(tk.Menu):
    def __init__(self, master):
        super().__init__(master)
        
        webhookMenu = tk.Menu(self)
        self.add_cascade(label = "Webhook", menu = webhookMenu )
        

class Frame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg = "white")
        
        self.grid_columnconfigure((0), uniform = "a", weight = 1)
        self.grid_rowconfigure((0,1, 2, 3), uniform = "a", weight = 1)
        
        self.entry = tk.Text(self, height = 9, font = "Helvetica 16")
        self.entry.grid(row = 0, column = 0, rowspan = 2, sticky = "n")
        
        self.btn = tk.Button(self, text = "SEND", borderwidth = 0, bg = "white", font = "bahnschrift")
        self.btn.grid(row = 4, column = 0)
        
        self.grid(row = 0, column = 0, sticky = "nswe")



App()