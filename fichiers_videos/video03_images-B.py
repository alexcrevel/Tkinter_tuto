from tkinter import *
from random import randrange

LARG=600
HAUT=400

fen=Tk()
cnv=Canvas(fen, width=LARG, height=HAUT, background='ivory')
cnv.pack()


logo=PhotoImage(file='python.gif')


for i in range(5):
    centre=(randrange(LARG), randrange(HAUT))
    id_image=cnv.create_image(centre, image=logo)
    print(id_image)
    

fen.mainloop() 


