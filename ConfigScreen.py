import tkinter as tk

# ConfigScreen will be place to view and modify server configs
class ConfigScreen(tk.Frame):
    def __init__(self, parent=None, master=None):
        tk.Frame.__init__(self,master)
        self.parent = parent
        self.master = master

        # buttons
        self.title = tk.Label(master, text="Config")
        self.backButton = tk.Button(master,text="Back to welcome screen", command=parent.goToWelcomeScreen)
        self.checkServerButton = tk.Button(master, text="Check Local Server", command=parent.checkLocalServer)

        # feedback
        self.sentLabel = tk.Label(master, text="Sent")
        self.clientSentText = tk.Text(master, width=50, height=10)
        self.receivedLabel = tk.Label(master, text="Received")
        self.clientReceivedText = tk.Text(master, width=50, height=10) #not pixels, lines -- dependent on font

    def hide(self):
        self.title.place_forget()
        self.backButton.place_forget()
        self.checkServerButton.place_forget()
        self.clientSentText.place_forget()
        self.sentLabel.place_forget()
        self.receivedLabel.place_forget()
        self.clientReceivedText.place_forget()

    def show(self):
        self.backButton.place(x=50, y=50)
        self.title.place(x=10, y=10)
        self.checkServerButton.place(x=50, y = 80)
        self.sentLabel.place(x=50, y=120)
        self.clientSentText.place(x=50, y=140)
        self.receivedLabel.place(x=400, y=120)
        self.clientReceivedText.place(x=400, y=140)

    def logSent(self, text):
        self.clientSentText.insert(tk.END, text + "\n")

    def logReceived(self, text):
        self.clientReceivedText.insert(tk.END, text + "\n")
