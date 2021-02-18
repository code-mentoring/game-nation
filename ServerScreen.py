import tkinter as tk

class ServerScreen(tk.Frame):
    def __init__(self, parent=None, master=None):
        tk.Frame.__init__(self,master)
        self.parent = parent
        self.master = master

        # buttons
        self.title = tk.Label(master, text="Server Config")
        self.backButton = tk.Button(master,text="Back to welcome screen", command=parent.goToWelcomeScreen)
        self.checkServerButton = tk.Button(master, text="Check Local Server", command=parent.checkLocalServer)
        
    def hide(self):
        self.title.place_forget()
        self.backButton.place_forget()
        self.checkServerButton.place_forget()

    def show(self):
        self.backButton.place(x=50, y=50)
        self.title.place(x=10, y=10)
        self.checkServerButton.place(x=50, y = 80)
