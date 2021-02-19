import tkinter as tk

from WelcomeScreen import *
from ConfigScreen import *
from Client import *

# The MainWindow class will own all of the other GUI elements (contained by "screens")
# It also owns the "Client" which will be the piece that talks to the server
# MainWindow will handle routing between UI components and server
class MainWindow(tk.Frame):
    def __init__(self, master= None):
        tk.Frame.__init__(self, master)
        self.master = master
        
        self.welcomeScreen = WelcomeScreen(self, master)
        self.configScreen = ConfigScreen(self, master)
        self.welcomeScreen.show()

        self.client = Client()

    def goToServerScreen(self):
        print("Going to config screen")
        self.welcomeScreen.hide()
        self.configScreen.show()

    def goToWelcomeScreen(self):
        print("Going to welcome screen")
        self.configScreen.hide()
        self.welcomeScreen.show()

    def checkLocalServer(self):
        self.configScreen.logSent("Checking for listening server...")
        success = self.client.check_server("localhost", 5000)
        if success:
            self.configScreen.logSent("Server is listening.")
        else:
            self.configScreen.logSent("No Server listening.")

