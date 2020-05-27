from tkinter import *
from random import randrange, shuffle

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

fenetre = Tk()
cnv = Canvas(fenetre, width=LARG, height=HAUT, bg="grey")
cnv.pack(padx=20, pady=10)


plateau = melanger_grille()

logos = []
for lang in LANG:
    fichier = "fichiers_videos/images/" + lang + ".gif"
    logo = PhotoImage(file=fichier)
    logos.append(logo)

x0=y0=SIDE/2

for ligne in range(NB_LIG):
    for col in range(NB_COL):
        centre = (col*SIDE + x0,ligne*SIDE + y0)
        numero = plateau[ligne][col]
        logo = logos[numero]
        id_image = cnv.create_image(centre, image=logo)



fenetre.mainloop()
