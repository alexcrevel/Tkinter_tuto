# --------------- Base : vidéo n°2 ------------------------
from tkinter import *

LARG=600
HAUT=400

fen=Tk()
cnv=Canvas(fen, width=LARG, height=HAUT, bg="ivory")
cnv.pack(side=LEFT)

btn=Button(fen, text="Nouveau")
btn.pack(padx=10, pady=10)
fen.mainloop()


