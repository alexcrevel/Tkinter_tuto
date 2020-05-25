from tkinter import *


# 3. Changer dimensions 
# SIDE, LARG, HAUT, COTE=120, PAD, SIDE, X0, Y0


COTE=120
NB_LIG=4
NB_COL=5


PAD=5
SIDE=COTE+2*PAD

LARG=NB_COL*SIDE
HAUT=NB_LIG*SIDE

X0=Y0=SIDE/2

fen=Tk()

# 1. Couleur
cnv=Canvas(fen, width=LARG, height=HAUT, background='gray')
cnv.pack()


# 2 ./images/cover
cover = PhotoImage(file="./images/cover.gif")


# 4. Schéma
# 5. Générer la grille

for lig in range(NB_LIG):
    for col in range(NB_COL):
        centre=(col*SIDE+X0, lig*SIDE+Y0)
        cnv.create_image(centre, image=cover)
    
fen.mainloop()


















