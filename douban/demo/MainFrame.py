# -*- coding:utf-8 -*-
from tkinter import *      
import chardet
import json  
import movieUI as movie
win=Tk()
canvas=Canvas(win,width=400,height=400,bg='yellow',scrollregion=(0,0,400,5000))
canvas.pack(fill=X,expand=True)
panel=Frame(canvas)
#panel.pack(side='left',fill=Y,expand=True)
with open('D:\A开发\Reptitle\douban\demo\movie.json','rb') as file:
    data=file.read().decode('utf-8')
    item=data.split('{')
    for i in item:
        if len(i) > 0:
            jsonStr=eval('{'+i) # turn str to dict
            m=movie.movieUI(panel)
            m.setContent(jsonStr['name'],jsonStr['rate'],jsonStr['comment'])
            m.pack(fill=BOTH)
scrolly=Scrollbar(canvas,orient=VERTICAL)
scrolly.place(x=380,width=20,height=400)
scrolly.config(command=canvas.yview)
canvas.config(yscrollcommand=scrolly.set)
canvas.create_window((77,-140), window=panel)  #create_window
win.title('豆瓣电影Top250')
win.geometry("400x400")
win.resizable(width=False,height=False)
win.mainloop()       