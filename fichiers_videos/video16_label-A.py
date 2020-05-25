# --------------- Base : vidéo n°15 ------------------------
from tkinter import *

LARG=600
HAUT=400

fen=Tk()
cnv=Canvas(fen, width=LARG, height=HAUT, bg="ivory")
cnv.pack(side=LEFT)

lbl=Label(fen, text=42, font="courier 20 bold")
lbl.pack(padx=10, pady=10)
fen.mainloop()


