from tkinter import *      
class movieUI(Frame):
    def setContent(self,name,rate,comment):
        Label(self,text=name,bg='pink').pack(side='top',fill=X)
        Label(self,text=rate+':'+comment,bg='Aqua').pack(side='bottom',fill=X)