# ---------------- Base : vidéo n°17 --------------------
from tkinter import *
from random import shuffle

# 1. pygame
import pygame

COTE = 120
PAD = 5
SIDE = COTE + PAD

NB_LIG = 2
NB_COL = 3

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
    # 5.a pygame 
    global cpt, couples
    
    item=ids_cover[lig][col]
    cnv.delete(item)
    if move[0] is None:
        move[0]=(lig, col)
    else:
        if move[0]==(lig, col):
            return
        cpt=cpt+1
        lbl['text']=cpt
        move[1]=(lig, col)
        i, j=move[0]
        if plateau[i][j]==plateau[lig][col]:
            plateau[i][j]=plateau[lig][col]=-1
            move[0]=move[1]=None
            
            # 4. pygame
            couples=couples+1
            if couples==NB_CARTES:
                cnv.after(500, applaudir)
            
        else:
            cnv.after(400, cacher, i,j, lig, col)

def cacher(i, j, lig, col):
    centre = (X0 + j * SIDE, Y0 + i * SIDE)
    ids_cover[i][j]=cnv.create_image(centre, image=cover)
    centre = (X0 + col * SIDE, Y0 + lig * SIDE)
    ids_cover[lig][col]=cnv.create_image(centre, image=cover)

    move[0]=move[1]=None
    
# 3. pygame
def applaudir():
    pygame.mixer.music.set_volume(0.75)
    pygame.mixer.music.play(-1)
    

def init():
    # 5.c pygame
    global plateau, ids_cover, move, cpt, couples
    plateau=melanger_grille()
    ids_cover=remplir(plateau)
    move=[None, None]
    cpt=0
    lbl['text']=0
    # 5b. pygame
    couples=0
    
    # 6 pygame
    pygame.mixer.music.stop()


def quitter():
    pygame.quit()
    fen.destroy()

# --------------- Les widgets ---------------
fen = Tk()

fen.protocol("WM_DELETE_WINDOW", quitter)

# Le canevas
cnv = Canvas(fen, width=LARG, height=HAUT, bg='gray')
cnv.pack(side=LEFT)

# Le bouton
btn=Button(fen, text="Nouveau", command=init)
btn.pack(padx=10, pady=10)
cnv.bind("<Button>", clic)

cover=PhotoImage(file="./images/cover.gif")


lbl=Label(fen, text=0, font="courier 20 bold")
lbl.pack(padx=10, pady=10)

# 2. pygame
pygame.mixer.init()
pygame.mixer.music.load("clap.wav")


# Action

logos=creer_logos()
init()


fen.mainloop()
