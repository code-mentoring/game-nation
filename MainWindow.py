import tkinter as tk

from WelcomeScreen import WelcomeScreen
from ServerScreen import ServerScreen
from Client import Client

class MainWindow(tk.Frame):
    def __init__(self, master= None):
        tk.Frame.__init__(self, master)
        self.master = master
        
        self.welcomeScreen = WelcomeScreen(self, master)
        self.serverScreen = ServerScreen(self, master)
        self.welcomeScreen.show()

        self.client = Client()

    def goToServerScreen(self):
        print("Going to server screen")
        self.welcomeScreen.hide()
        self.serverScreen.show()

    def goToWelcomeScreen(self):
        print("Going to welcome screen")
        self.serverScreen.hide()
        self.welcomeScreen.show()

    def checkLocalServer(self):
        self.client.check_server("localhost", 5000)
