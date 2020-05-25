# ---------------- Base : vidéo n°14 --------------------
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
    P=[[0,3,3, 8,5],[7,1,2, 9,9],
       [7,4,8, 2,0],[4,5,6,1,6]]
    return P


def creer_logos():
    # Liste logos
    logos=[]

    for i in range(NB_CARTES):
        lang=LANG[i]
        nom="./images/"+lang+".gif"
        logo=PhotoImage(file=nom)
        logos.append(logo)
    return logos


def remplir(plateau):
    ids_cover=[]
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
    return ids_cover



def clic(event):
    if move[1] is not None:
        return
    X=event.x
    Y= event.y
    col=X//SIDE
    lig=Y//SIDE
    if plateau[lig][col]!=-1:
        traiter_clic(lig, col)

def traiter_clic(lig, col):
    item=ids_cover[lig][col]
    cnv.delete(item)
    if move[0] is None:
        move[0]=(lig, col)
    else:
        if move[0]==(lig, col):
            return
        move[1]=(lig, col)
        i, j=move[0]
        if plateau[i][j]==plateau[lig][col]:
            plateau[i][j]=plateau[lig][col]=-1
            move[0]=move[1]=None
        else:
            cnv.after(400, cacher, i,j, lig, col)

def cacher(i, j, lig, col):
    centre = (X0 + j * SIDE, Y0 + i * SIDE)
    ids_cover[i][j]=cnv.create_image(centre, image=cover)
    centre = (X0 + col * SIDE, Y0 + lig * SIDE)
    ids_cover[lig][col]=cnv.create_image(centre, image=cover)

    move[0]=move[1]=None

def init():
    global plateau, ids_cover, move
    plateau=melanger_grille()
    ids_cover=remplir(plateau)
    move=[None, None]

fen = Tk()
cnv = Canvas(fen, width=LARG, height=HAUT, bg='gray')
cnv.pack(side=LEFT)
logos=creer_logos()
cover=PhotoImage(file="./images/cover.gif")

init()

cnv.bind("<Button>", clic)

btn=Button(fen, text="Nouveau", command=init)
btn.pack(padx=10, pady=10)






fen.mainloop()
