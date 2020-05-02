import numpy as np
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import random as r
import time
tk=Tk()
Label(tk,text='Player 1:').grid(row=0)
Label(tk,text='Player2:').grid(row=1)
e1=Entry(tk)
e2=Entry(tk)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
active_play=1
tk.title("TIC TAC TOE :player 1")
style=ttk.Style()
style.theme_use('classic')
p1=[]
p2=[]

bu1=ttk.Button(tk,text=' ')
bu1.grid(row=2,column=0,sticky='snew',ipadx=40,ipady=40)
bu1.config(command=lambda: ButtonClick(1))
bu2=ttk.Button(tk,text=' ')
bu2.grid(row=2,column=1,sticky='snew',ipadx=40,ipady=40)
bu2.config(command=lambda: ButtonClick(2))
bu3=ttk.Button(tk,text=' ')
bu3.grid(row=2,column=2,sticky='snew',ipadx=40,ipady=40)
bu3.config(command=lambda: ButtonClick(3))
bu4=ttk.Button(tk,text='')
bu4.grid(row=3,column=0,sticky='snew',ipadx=40,ipady=40)
bu4.config(command=lambda: ButtonClick(4))
bu5=ttk.Button(tk,text=' ')
bu5.grid(row=3,column=1,sticky='snew',ipadx=40,ipady=40)
bu5.config(command=lambda: ButtonClick(5))
bu6=ttk.Button(tk,text=' ')
bu6.grid(row=3,column=2,sticky='snew',ipadx=40,ipady=40)
bu6.config(command=lambda: ButtonClick(6))
bu7=ttk.Button(tk,text=' ')
bu7.grid(row=4,column=0,sticky='snew',ipadx=40,ipady=40)
bu7.config(command=lambda: ButtonClick(7))
bu8=ttk.Button(tk,text=' ')
bu8.grid(row=4,column=1,sticky='snew',ipadx=40,ipady=40)
bu8.config(command=lambda: ButtonClick(8))
bu9=ttk.Button(tk,text=' ')
bu9.grid(row=4,column=2,sticky='snew',ipadx=40,ipady=40)
bu9.config(command=lambda: ButtonClick(9))

def ButtonClick(id):
    global active_play
    global p1
    global p2
    if(active_play==1):
        play_game(id,"X")
        p1.append(id)
        tk.title("Tic tac toe :Player 2")
        active_play=2
        Check_win()
        print(p1)
    elif(active_play==2):
        play_game(id,"O")
        p2.append(id)
        tk.title("Tic tac toe :Player 1")
        active_play=1
        Check_win()
        print(p2)

def play_game(id,PlayerSymbol):
    if(id==1):
        bu1.config(text=PlayerSymbol)
        bu1.state(['disabled'])
    if(id==2):
        bu2.config(text=PlayerSymbol)
        bu2.state(['disabled'])
    if(id==3):
        bu3.config(text=PlayerSymbol)
        bu3.state(['disabled'])
    if(id==4):
        bu4.config(text=PlayerSymbol)
        bu4.state(['disabled'])
    if(id==5):
        bu5.config(text=PlayerSymbol)
        bu5.state(['disabled'])
    if(id==6):
        bu6.config(text=PlayerSymbol)
        bu6.state(['disabled'])
    if(id==7):
        bu7.config(text=PlayerSymbol)
        bu7.state(['disabled'])
    if(id==8):
        bu8.config(text=PlayerSymbol)
        bu8.state(['disabled'])
    if(id==9):
        bu9.config(text=PlayerSymbol)
        bu9.state(['disabled'])
    
def Check_win():
    c=0
    if(1 in p1 and 2 in p1 and 3 in p1) or (1 in p1 and 4 in p1 and 7 in p1 ) or (1 in p1 and 5 in p1 and 9 in p1) or (3 in p1 and 5 in p1 and 7 in p1) or (4 in p1 and 5 in p1 and 6 in p1) or (7 in p1 and 8 in p1 and 9 in p1) or (2 in p1 and 5 in p1 and 8 in p1) or (3 in p1 and 6 in p1 and 9 in p1):
        c=1
    elif(1 in p2 and 2 in p2 and 3 in p2) or (1 in p2 and 4 in p2 and 7 in p2 ) or (1 in p2 and 5 in p2 and 9 in p2) or (3 in p2 and 5 in p2 and 7 in p2) or(4 in p2 and 5 in p2 and 6 in p2) or (7 in p2 and 8 in p2 and 9 in p2) or (2 in p2 and 5 in p2 and 8 in p2) or (3 in p2 and 6 in p2 and 9 in p2):
        c=2

    if(c==1):
        messagebox.showinfo(title="Congrats", message="Player 1 wins")
    if(c==2):
        messagebox.showinfo(title="Congrats",message="Player 2 wins")
    elif(len(p1)+len(p2)==9):
         messagebox.showinfo(title="Draw",message="Bad Luck")

tk.mainloop()
