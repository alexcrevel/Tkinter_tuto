from tkinter import *
from random import randrange

COTE = 120
PAD = 5
SIDE = COTE+2*PAD

NB_LIG = 4
NB_COL = 5

LARG = NB_COL*SIDE
HAUT = NB_LIG*SIDE

fenetre = Tk()
cnv = Canvas(fenetre, width=LARG, height=HAUT, bg="grey")
cnv.pack(padx=20, pady=10)

logo = PhotoImage(file="fichiers_videos\images\cover.gif")
x0=y0=SIDE/2

for ligne in range(NB_LIG):
    for col in range(NB_COL):
        centre = (col*SIDE + x0,ligne*SIDE + y0)
        id_image = cnv.create_image(centre, image=logo)

print("test")



fenetre.mainloop()
