from tkinter import *

# -----------
from random import randrange
# ------------
repet=12

DIM=100

LARG=repet*DIM
HAUT=DIM

fen=Tk()
cnv=Canvas(fen, width=LARG, height=HAUT, background='ivory')
cnv.pack(pady=20)


logo=PhotoImage(file='python.gif')

X0=DIM/2
Y0=DIM/2

for i in range(repet):
    centre=(X0+i*DIM, Y0)
    id_image=cnv.create_image(centre, image=logo)
    print(id_image)

# ------------------
i=randrange(1, repet+1)
print()
print(i)
cnv.delete(i)
# ------------------

 

fen.mainloop() 
