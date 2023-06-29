# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 09:05:36 2023

@author: hank1

pip3 install gTTS==2.2.1
pip3 install pygame==1.9.6

"""

from os.path import exists
import tkinter as tk
from gtts import gTTS
from pygame import mixer
import csv 
import random 
# def
j=0
def click_callword():
    global j
    #i=next(r)        
    #ST=": ".join(i[2:])
    ST=": ".join(LIST[j])
    textvar.set(ST)
    j=j+1
def click_voice():
    j=random.randrange(10000000)
    st=textvar.get()
    #print(st)
    #textvarcheck.set(textvar.get()) 
    tts=gTTS(text=textvar.get(),lang="en")
    #if not exists('D:/TEMP/temp/en{}.mp3'.format(j)):        
    tts.save('D:/TEMP/temp/en{}.mp3'.format(j))
    mixer.init()
    mixer.music.load('D:/TEMP/temp/en{}.mp3'.format(j))
    mixer.music.play(loops=0)
    
    #mixer.music.unload()  #2.0.0才有
    #固定key不妥，這樣自行輸入會出問題,因此換成隨機
def click_search():    
    st=textvar.get()
    str_match=list(filter(lambda x: st in x,LIST2))
    #print(str_match)
    st2="\n".join(list(str_match))
    
    search.delete(1.0, "end")
    search.insert(tk.INSERT,st2)
def click_voice_search():
    st=search.get(1.0, "end")
    j=random.randrange(10000000)
    tts=gTTS(text=st,lang="en")
    #if not exists('D:/TEMP/temp/en{}.mp3'.format(j)):        
    tts.save('D:/TEMP/temp/en{}.mp3'.format(j))
    mixer.init()
    mixer.music.load('D:/TEMP/temp/en{}.mp3'.format(j))
    mixer.music.play(loops=0)    
# 定義視窗
win=tk.Tk() #視窗
win.geometry("600x450")
win.configure(bg="white")

win.title("英語學習")
label2=tk.Label(win,text="學習英語中",fg="red",bg="cyan",font=("微軟正黑體",20))
label2.pack()

textvar=tk.StringVar()
textvar.set("我的輸入文字方塊")
entry=tk.Entry(win,textvariable=textvar,width=40,font=("微軟正黑體",15))
entry.place(x=50,y=250)

button_word=tk.Button(win,text="換單字",fg="yellow",bg="blue",width=10,font=("微軟正黑體",16),command=click_callword)
button_word.place(x=150,y=300)
button_voice=tk.Button(win,text="朗讀",fg="yellow",bg="blue",width=10,font=("微軟正黑體",16),command=click_voice)
button_voice.place(x=300,y=300)
button_search=tk.Button(win,text="找單字",fg="yellow",bg="blue",width=10,font=("微軟正黑體",16),command=click_search)
button_search.place(x=225,y=350)

button_voice=tk.Button(win,text="朗讀搜尋結果",fg="yellow",bg="blue",width=10,font=("微軟正黑體",16),command=click_voice_search)
button_voice.place(x=400,y=350)

textvar_search=tk.StringVar()
textvar_search.set("我的搜尋結果")
#search=tk.Entry(win,textvariable=textvar_search,width=40,font=("微軟正黑體",15))
search=tk.Text(win,width=40,height=3,font=("微軟正黑體",15))

search.place(x=50,y=100)
"""
textvarcheck=tk.StringVar()
textvarcheck.set("132")   
text4=tk.Entry(win,textvariable=textvarcheck,width=40,font=("微軟正黑體",15))
text4.place(x=50,y=100)
"""

LIST=[]
LIST2=[]
fin=open("words.csv","r",encoding="utf-8")
r=csv.reader(fin)
for i in r:
    LIST.append([i[2],i[3]])
    LIST2.append(i[2]+ ":" + i[3])

win.mainloop()    
fin.close()