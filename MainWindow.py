import tkinter as tk

from WelcomeScreen import WelcomeScreen
from ServerScreen import ServerScreen

class MainWindow(tk.Frame):
    def __init__(self, master= None):
        tk.Frame.__init__(self, master)
        self.master = master
        
        self.welcomeScreen = WelcomeScreen(self, master)
        self.serverScreen = ServerScreen(self, master)
        self.welcomeScreen.show()

    def goToServerScreen(self):
        print("Going to server screen")
        self.welcomeScreen.hide()
        self.serverScreen.show()

    def goToWelcomeScreen(self):
        print("Going to welcome screen")
        self.serverScreen.hide()
        self.welcomeScreen.show()
