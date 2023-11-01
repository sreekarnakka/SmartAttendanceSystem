from tkinter import *
from tkinter import messagebox

tkWindow = Tk()
tkWindow.geometry('400x150')
tkWindow.title('AI ATTENDANCE SYSTEM')


def showMsg():
    tkWindow = Tk()
    tkWindow.geometry('400x150')
    tkWindow.title('AI ATTENDANCE SYSTEM')
    button = Button(tkWindow,
                    text='LIVE CAM',
                    command=showMsg)
    button.pack()


button = Button(tkWindow,
                text='Take Attendance',
                command=showMsg)
button.pack()

tkWindow.mainloop()