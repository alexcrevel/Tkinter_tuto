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


ids_cover=[]
cover=PhotoImage(file="./images/cover.gif")

# Placement des images
for lig in range(NB_LIG):
    L=[]
    for col in range(NB_COL):
        centre = (X0 + col * SIDE, Y0 + lig * SIDE)
        i=plateau[lig][col]
        logo=logos[i]
        cnv.create_image(centre, image=logo)
        id_cover=cnv.create_image(centre, image=cover)
        L.append(id_cover)
    ids_cover.append(L)

def clic(event):
    X=event.x
    Y= event.y
    col=X//SIDE
    lig=Y//SIDE
    id_cover=ids_cover[lig][col]
    cnv.delete(id_cover)
    cnv.after(1000, recouvrir, (lig, col))
   
def recouvrir(pos):
    lig, col=pos
    c = (X0 + col * SIDE, Y0 + lig * SIDE)
    id_cover=cnv.create_image(c, image=cover)
    ids_cover[lig][col]=id_cover
    
cnv.bind("<Button>", clic)

fen.mainloop() 
