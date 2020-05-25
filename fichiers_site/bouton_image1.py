from tkinter import *
from random import randrange

SIDE=400
root = Tk()
cnv = Canvas(root, width=SIDE, height=SIDE, bg='ivory')
cnv.pack()

logo = PhotoImage(file="python.gif")

def show():
    center= (randrange(SIDE),randrange(SIDE))
    cnv.create_image(center, image=logo)    

btn=Button(root, text="Nouveau", command=show)
btn.pack()

root.mainloop()
