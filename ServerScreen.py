import tkinter as tk

class ServerScreen(tk.Frame):
    def __init__(self, parent=None, master=None):
        tk.Frame.__init__(self,master)
        self.parent = parent
        self.master = master

        # title text
        self.title = tk.Label(master, text="Server Config")

        # server button
        self.backButton = tk.Button(master,text="Back to welcome screen", command=parent.goToWelcomeScreen)
        
    def hide(self):
        self.title.place_forget()
        self.backButton.place_forget()

    def show(self):
        self.backButton.place(x=50, y=50)
        self.title.place(x=10, y=10)
