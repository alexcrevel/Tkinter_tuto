from tkinter import *
from random import shuffle, randrange

PICT_SIZE=120
PAD=10
SIDE=PICT_SIZE+PAD

NB_LINES=4
NB_COLS=5
NB_PICT=NB_LINES*NB_COLS//2
WIDTH=SIDE*NB_COLS
HEIGHT=SIDE*NB_LINES
X0=Y0=SIDE//2

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

def fill(cnv, board, cover, logos, ids_cover):
    # Placement des images
    for line in range(NB_LINES):
        for col in range(NB_COLS):
            center=(X0+col*SIDE, Y0+line*SIDE)
            nro_image=board[line][col]
            mon_image=logos[nro_image]
            cnv.create_image(center, image=mon_image)
            id_cover=cnv.create_image(center, image=cover)
            ids_cover[line][col] = id_cover

def play():
    root=Tk()
    cnv=Canvas(root, width=WIDTH, height=HEIGHT, bg='gray')
    cnv.pack()

    cover = PhotoImage(file="./images/cover.gif")
    logos=[PhotoImage(file="./images/%s.gif" %filename) for filename in LANG]
    ids_cover=[[None for j in range(NB_COLS)] for i in range(NB_LINES)]
    board=make_board()

    print(board)
    fill(cnv, board, cover, logos, ids_cover)

    line=randrange(NB_LINES)
    col=randrange(NB_COLS)
    print(line, col)
    im_id=ids_cover[line][col]
    cnv.delete(im_id)

    root.mainloop()
    
play()
