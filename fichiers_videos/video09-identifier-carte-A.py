# --------------- à partir de vidéo 5 ------------------------------------
from tkinter import *

PICT_SIZE=120
PAD=10
SIDE=PICT_SIZE+PAD

NB_LINES=4
NB_COLS=5
WIDTH=SIDE*NB_COLS
HEIGHT=SIDE*NB_LINES
X0=Y0=SIDE//2

root=Tk()
cnv=Canvas(root, width=WIDTH, height=HEIGHT, bg='gray')
cnv.pack()

cover = PhotoImage(file="./images/cover.gif")


for line in range(NB_LINES):
    for col in range(NB_COLS):
        cnv.create_image(X0+col*SIDE, Y0+line*SIDE, image=cover)

def clic(event):
    X=event.x
    Y= event.y
    col=X//SIDE
    lig=Y//SIDE
    print(lig, col)
    
    

cnv.bind("<Button>", clic)




root.mainloop()
