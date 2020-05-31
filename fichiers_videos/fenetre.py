from tkinter import *
from random import randrange, shuffle
import pygame

LANG = ["c", "cpp", "go", "java", "js", "ocaml", 
        "php", "python", "ruby", "scratch"]

COTE = 120
PAD = 5
SIDE = COTE+2*PAD

NB_LIG = 4
NB_COL = 5
NB_CARTES = NB_LIG*NB_COL//2

LARG = NB_COL*SIDE
HAUT = NB_LIG*SIDE

X0=Y0=SIDE/2

def melanger_grille():
    cartes = list(range(NB_CARTES))*2
    shuffle(cartes)

    P = []
    k = 0
    for lig in range(NB_LIG):
        L = []
        for col in range(NB_COL):
            L.append(cartes[k])
            k += 1
        P.append(L)
    return P

def creer_logos():
    logos = []
    for lang in LANG:
        fichier = "fichiers_videos/images/" + lang + ".gif"
        logo = PhotoImage(file=fichier)
        logos.append(logo)
    return logos

def remplir(plateau):
    ids_cover=[]
    for ligne in range(NB_LIG):
        L=[]
        for col in range(NB_COL):
            centre = (col*SIDE + X0,ligne*SIDE + Y0)
            numero = plateau[ligne][col]
            logo = logos[numero]
            cnv.create_image(centre, image=logo)
            id_cover = cnv.create_image(centre, image=cover)
            L.append(id_cover)
        ids_cover.append(L)
    return ids_cover

def clic(event):
    global cpt
    if move[1] is not None:
        return
    X=event.x
    Y= event.y
    col=X//SIDE
    lig=Y//SIDE
    if plateau[lig][col] != -1:
        traiter_clic(lig, col)


def traiter_clic(lig, col):
    global cpt, couples
    item = ids_cover[lig][col]
    cnv.delete(item)
    if move[0] is None:
        move[0] = (lig, col)
    else:
        if move[0] == (lig, col):
            return
        cpt += 1
        lbl["text"]=cpt
        move[1] = (lig, col)
        i, j = move[0]
        if plateau[i][j] == plateau[lig][col]:
            plateau[i][j] = plateau[lig][col] = -1
            move[0] = move[1] = None
            
            couples += 1
            if couples == NB_CARTES:
                cnv.after(500, applaudir)
        
        else:
            cnv.after(400, cacher, i, j , lig, col)

def cacher(i, j, lig, col):
    centre = (j*SIDE + X0,i*SIDE + Y0)
    ids_cover[i][j] = cnv.create_image(centre, image=cover)
    centre = (col*SIDE + X0,lig*SIDE + Y0)
    ids_cover[lig][col] = cnv.create_image(centre, image=cover)
    move[0] = move[1] = None

def applaudir():
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

def init():
    global plateau, ids_cover, move, cpt, couples
    plateau = melanger_grille()
    ids_cover = remplir(plateau)
    move = [None, None]
    cpt = 0
    lbl["text"] = 0
    couples = 0
    pygame.mixer.music.stop()



fenetre = Tk()
cnv = Canvas(fenetre, width=LARG, height=HAUT, bg="grey")
cnv.pack(side=LEFT)
button = Button(fenetre, text="Nouveau", command=init)
button.pack(padx=10, pady=10)

cover = PhotoImage(file="fichiers_videos/images/cover.gif")
cpt = 0

lbl = Label(fenetre, text=0, font="courier 20 bold")
lbl.pack(padx=10, pady=10)

couples = 0

pygame.mixer.init()
pygame.mixer.music.load("fichiers_videos/clap.wav")

logos = creer_logos()

init()

cnv.bind("<Button>", clic)

fenetre.mainloop()
