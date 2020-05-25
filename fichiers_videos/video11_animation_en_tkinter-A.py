# ------------- D'après vidéo n°3 -----------------------------

from tkinter import *
from random import randrange
SIDE=400
SIDE=400

fen=Tk()
cnv=Canvas(fen, width=SIDE, height=SIDE, background='ivory')
cnv.pack(padx=5, pady=5)
logo=PhotoImage(file="python.gif")

def action(centre):
    cnv.create_image(centre, image=logo)

centre=(randrange(SIDE), randrange(SIDE))
cnv.after(1000, action, centre)
centre=(randrange(SIDE), randrange(SIDE))
cnv.after(2000, action, centre)
centre=(randrange(SIDE), randrange(SIDE))
cnv.after(3000, action, centre)
centre=(randrange(SIDE), randrange(SIDE))
cnv.after(4000, action, centre)
centre=(randrange(SIDE), randrange(SIDE))
cnv.after(5000, action, centre)
centre=(randrange(SIDE), randrange(SIDE))
cnv.after(6000, action, centre)

print("FIN DU CODE")

fen.mainloop()























