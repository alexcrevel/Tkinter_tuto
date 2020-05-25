# --------------- Base : vidéo n°2 ------------------------

from random import randrange
from tkinter import *

LARG=600
HAUT=400

fen=Tk()
cnv=Canvas(fen, width=LARG, height=HAUT, bg="ivory")
cnv.pack(side=LEFT)


logo=PhotoImage(file='python.gif')


def show():
    x=randrange(LARG)
    y=randrange(HAUT)    
    cnv.create_image((x,y), image=logo)

btn=Button(fen, text="Nouveau", command=show)
btn.pack(pady=5, padx=2)

fen.mainloop()
