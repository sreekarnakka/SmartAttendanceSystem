from tkinter import *
import ultimate

class BButtons:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame, text="Take Attendance", command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.printButton = Button(frame, text="Quit", command=frame.quit)
        self.printButton.pack(side=LEFT)

    def printMessage(selfself):
        ultimate


root = Tk()
b = BButtons(root)
root.mainloop()