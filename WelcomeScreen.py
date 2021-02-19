import tkinter as tk

# Welcome screen will display basic server config info
# And buttons to go to config screen or connect to server
class WelcomeScreen(tk.Frame):
    def __init__(self, parent=None, master=None):
        tk.Frame.__init__(self,master)
        self.parent = parent
        self.master = master

        # title text
        self.title = tk.Label(master, text="Game-nation")

        # server button
        self.serverButton = tk.Button(master,text="Server Config", command=parent.goToServerScreen)
        
    def hide(self):
        self.title.place_forget()
        self.serverButton.place_forget()

    def show(self):
        self.serverButton.place(x=50, y=50)
        self.title.place(x=10, y=10)
