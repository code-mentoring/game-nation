from tkinter import *
from MainWindow import *
import sys
from subprocess import Popen, PIPE

def main(argv : list):

    # only spin up server if in debug mode
    debugMode = argv.count("debug") > 0
    if debugMode:
        p = Popen(['node', 'test-server.js'], stdout=PIPE, stderr=PIPE)

    # create GUI and start main event loop
    root = Tk()
    mainWindow = MainWindow(root)
    root.mainloop()

    # cleanup debug server
    if debugMode: 
        p.kill()


if __name__ == "__main__":
   main(sys.argv[1:])
