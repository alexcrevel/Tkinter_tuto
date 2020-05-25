from tkinter import *

LARG=600
HAUT=400

fen=Tk()
cnv=Canvas(fen, width=LARG, height=HAUT, background='ivory')
cnv.pack(side=LEFT)

lbl=Label(fen, text=0, width=2, font="courier 20 bold")
lbl.pack(padx=10, pady=10)

logo=PhotoImage(file="python.gif")

def clic(event):
    cnv.create_image((event.x, event.y), image=logo)
    lbl['text']=lbl['text']+1
    

cnv.bind("<Button>", clic)

fen.mainloop() 
