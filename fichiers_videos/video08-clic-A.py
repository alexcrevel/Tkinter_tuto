from tkinter import *

LARG=600
HAUT=400

fen=Tk()
cnv=Canvas(fen, width=LARG, height=HAUT, background='ivory')
cnv.pack()

def clic(event):
    print(event.x, event.y)

cnv.bind("<Button>", clic)

fen.mainloop()
