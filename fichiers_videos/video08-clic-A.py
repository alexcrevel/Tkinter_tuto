from tkinter import *

LARG=600
HAUT=400

fen=Tk()
cnv=Canvas(fen, width=LARG, height=HAUT, background='ivory')
cnv.pack()

logo = PhotoImage(file="fichiers_videos/images/python.gif")
id_image = 0

def clic(event):
    global id_image
    cnv.delete(id_image)
    centre = (event.x, event.y)
    id_image = cnv.create_image(centre, image=logo)

cnv.bind("<Button>", clic)

fen.mainloop()
