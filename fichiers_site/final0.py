from tkinter import *
from random import shuffle

PICT_SIZE=120
PAD=10
SIDE=PICT_SIZE+PAD

NB_LINES=4
NB_COLS=5
WIDTH=SIDE*NB_COLS
HEIGHT=SIDE*NB_LINES
X0=Y0=SIDE//2
NB_PICT=NB_LINES*NB_COLS//2
LANG=['c', 'cpp', 'go', 'java', 'js', 'ocaml', 
      'php', 'python', 'ruby', 'scratch']

def make_board():
    L=[v % NB_PICT for v in range(2*NB_PICT)]
    shuffle(L)
    board=[]
    k=0
    for line in range(NB_LINES):
        row=[]
        for col in range(NB_COLS):
            row.append(L[k])
            k+=1
        board.append(row)
    return board

def fill(cnv, images, board, cover, ids_cover):
    for line in range(NB_LINES):
        for col in range(NB_COLS):
            center=(X0+col*SIDE, Y0+line*SIDE)
            k=board[line][col]
            cnv.create_image(center, image=images[k])
            ids_cover[line][col]=cnv.create_image(center, image=cover)

def lin_col(x, y):
    return (y//SIDE, x//SIDE)

def clic(event):
    lin, col = lin_col(event.x, event.y)
    print(lin, col)

root=Tk()
cnv=Canvas(root, width=WIDTH, height=HEIGHT, bg='gray42')
cnv.pack()
cnv.bind("<Button>", clic)

cover = PhotoImage(file="./images/cover.gif")
images=[PhotoImage(file="./images/%s.gif" %filename) for filename in LANG]
ids_cover=[[None for j in range(NB_COLS)] for i in range(NB_LINES)]

board=make_board()
fill(cnv, images, board, cover, ids_cover)
root.mainloop()
