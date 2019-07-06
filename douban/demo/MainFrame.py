# -*- coding:utf-8 -*-
from tkinter import *      
import chardet
import json  
win=Tk()
with open('D:\A开发\Reptitle\douban\demo\movie.json','rb') as file:
    data=file.read().decode('utf-8')
    item=data.split('{')
    print(item[1][9:19])
    l = Label(win, text=item[1][9], bg='green', font=('Arial', 12), width=30, height=2)

win.title('豆瓣电影Top250')
win.geometry("400x400")
win.resizable(width=False,height=False)
l.pack()
win.mainloop()       