from tkinter import *
from random import randrange

SIDE=400
root = Tk()
cnv = Canvas(root, width=SIDE, height=SIDE)
cnv.pack()

logo = PhotoImage(file="python.gif")

for i in range(5):
    centre= (randrange(SIDE),randrange(SIDE))
    cnv.create_image(centre, image=logo)

root.mainloop()
