from random import shuffle

NB_LINES=4
NB_COLS=5
NB_PICT=NB_LINES*NB_COLS // 2

L=[v % NB_PICT for v in range(2*NB_PICT)]
shuffle(L)
print(L)

board=[]
k=0
for line in range(NB_LINES):
    row=[]
    for col in range(NB_COLS):
        row.append(L[k])
        k+=1
    board.append(row)
    
print(board)
