# -*- coding:utf-8 -*-
from tkinter import *      
import chardet
import json  
import movieUI as movie
win=Tk()
lb=Listbox(win,bg='pink')
with open('D:\A开发\Reptitle\douban\demo\movie.json','rb') as file:
    data=file.read().decode('utf-8')
    item=data.split('{')
    for i in item:
        if len(i) > 0:
            jsonStr=eval('{'+i) # turn str to dict
            lb.insert('end',jsonStr['rate']+'/'+jsonStr['name'])
scrolly=Scrollbar(win)
scrolly.pack(side='right',fill=Y)
lb['yscrollcommand'] = scrolly.set
scrolly['command'] = lb.yview

win.title('豆瓣电影Top250')
win.geometry("400x400")
lb.pack(side='left',fill=BOTH,expand=True)
win.resizable(width=False,height=False)
win.mainloop()       