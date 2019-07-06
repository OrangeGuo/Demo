from tkinter import *      
class movieUI(Frame):
    def setContent(self,name,rate,comment):
        Label(self,text=name).pack(side='top')
        Label(self,text=rate+':'+comment).pack(side='bottom')