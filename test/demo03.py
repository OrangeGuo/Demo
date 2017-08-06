from tkinter import *


class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createwidgets()

    def createwidgets(self):
        self.helloLabel = Label(self, text='hello,world!')
        self.helloLabel.pack()
        self.exit = Button(self, text='quit', command=self.quit)
        self.exit.pack()


app = Application()
app.mainloop()

