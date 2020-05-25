from tkinter import *
from random import randrange

SIDE=400
root = Tk()
cnv = Canvas(root, width=SIDE, height=SIDE)
cnv.pack()

logo = PhotoImage(file="python.gif")

for i in range(5):
    x, y= randrange(SIDE),randrange(SIDE)
    id_image=cnv.create_image(x, y, image=logo)
    print(id_image)
    
root.mainloop()
