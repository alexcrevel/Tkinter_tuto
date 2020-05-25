from tkinter import *

LARG=600
HAUT=400

fen=Tk()
cnv=Canvas(fen, width=LARG, height=HAUT, background='ivory')
cnv.pack()

logo=PhotoImage(file="python.gif")
id_image=0

def clic(event):
    global id_image
    cnv.delete(id_image)
    id_image=cnv.create_image((event.x, event.y), image=logo)
    print(event.x, event.y)

cnv.bind("<Button>", clic)

fen.mainloop() 
