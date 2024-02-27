import tkinter as tk
from tkinter import ttk
from funcs import sendMsg


class App(tk.Tk):    
    
    WEBHOOK_URL = ""
    
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

    def setWebhookWindow():
        
        def setWebhookBtn():
            App.WEBHOOK_URL = webhook.get()
            print(App.WEBHOOK_URL)
            setWebhook.destroy()
            
        setWebhook = tk.Toplevel()
        setWebhook.title("Webhook")
        setWebhook.resizable(0, 0)
        setWebhook.geometry("300x60")
        setWebhook.iconbitmap("discord.ico")
        
        webhook = tk.StringVar()
        
        setWebhook.grid_columnconfigure((0), uniform = "a", weight = 1)
        setWebhook.grid_rowconfigure((0,1), uniform = "a", weight = 1)        
        
        entry = ttk.Entry(setWebhook, width = 45, textvariable = webhook)
        entry.grid(row = 0, column = 0)
        
        btn = ttk.Button(setWebhook, text = "Set", command = setWebhookBtn)
        btn.grid(row = 1, column = 0)
        
        setWebhook.mainloop()

class Menu(tk.Menu):
    def __init__(self, master):
        super().__init__(master)
        
        webhookMenu = tk.Menu(self, tearoff = 0)
        webhookMenu.add_command(label = "Set", command = App.setWebhookWindow)
        
        self.add_cascade(label = "Webhook", menu = webhookMenu )
      
class Frame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg = "white")
        
        self.grid_columnconfigure((0), uniform = "a", weight = 1)
        self.grid_rowconfigure((0,1, 2, 3), uniform = "a", weight = 1)
        
        self.textbox = tk.Text(self, height = 9, font = "Helvetica 16")
        self.textbox.grid(row = 0, column = 0, rowspan = 2, sticky = "n")
        
        self.btn = tk.Button(self, text = "SEND", borderwidth = 0, bg = "white", font = "bahnschrift", command = lambda: sendMsg(App.WEBHOOK_URL, self.textbox.get("1.0", tk.END)))
        self.btn.grid(row = 4, column = 0)
        
        self.grid(row = 0, column = 0, sticky = "nswe")


App()