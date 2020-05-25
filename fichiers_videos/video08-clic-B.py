from tkinter import *

LARG=600
HAUT=400

fen=Tk()
cnv=Canvas(fen, width=LARG, height=HAUT, background='ivory')
cnv.pack()

logo=PhotoImage(file="python.gif")

def clic(event):
    id_image=cnv.create_image((event.x, event.y), image=logo)
    print(event.x, event.y)

cnv.bind("<Button>", clic)

fen.mainloop() 
