# ============================= Basé sur Vidéo 9 =================================

from tkinter import *
from random import shuffle

COTE = 120
PAD = 5
SIDE = COTE + PAD

NB_LIG = 4
NB_COL = 5

LARG = SIDE * NB_COL
HAUT = SIDE * NB_LIG
X0 = Y0 = SIDE // 2

NB_CARTES=NB_LIG*NB_COL//2

LANG=['c', 'cpp', 'go', 'java', 'js', 'ocaml',
      'php', 'python', 'ruby', 'scratch']

def melanger_grille():
    cartes=list(range(NB_CARTES))*2
    shuffle(cartes)

    P=[]
    k=0
    for lig in range(NB_LIG):
        L=[]
        for col in range(NB_COL):
            L.append(cartes[k])
            k+=1
        P.append(L)
    return P


fen = Tk()
cnv = Canvas(fen, width=LARG, height=HAUT, bg='gray')
cnv.pack()

plateau=melanger_grille()

# Liste logos
logos=[]

for i in range(NB_CARTES):
    lang=LANG[i]
    nom="./images/"+lang+".gif"
    logo=PhotoImage(file=nom)
    logos.append(logo)

# Placement des images
for lig in range(NB_LIG):
    for col in range(NB_COL):
        centre = (X0 + col * SIDE, Y0 + lig * SIDE)
        i=plateau[lig][col]
        logo=logos[i]
        cnv.create_image(centre, image=logo)


def clic(event):
    X=event.x
    Y= event.y
    col=X//SIDE
    lig=Y//SIDE
    print(lig, col)
    nro=plateau[lig][col]
    lang=LANG[nro]
    print(lang)
    print("----------")

cnv.bind("<Button>", clic)

# TODO
# 1. Définir cover
# 2. Couvrir cartes + liste d'id
# 3. clic : retirer couverture




fen.mainloop() 
