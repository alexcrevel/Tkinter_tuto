from tkinter import *

PICT_SIZE=120
PAD=10
SIDE=PICT_SIZE+PAD

NB_LINES=4
NB_COLS=5
WIDTH=SIDE*NB_COLS
HEIGHT=SIDE*NB_LINES

root=Tk()
cnv=Canvas(root, width=WIDTH, height=HEIGHT, bg='gray42')
cnv.pack(side=LEFT)

btn=Button(root, text="Nouvelle\npartie", font="Arial 12")
btn.pack(padx=20, pady=20)

lbl=Label(root, text=42, font="courier 20 bold")
lbl.pack()

root.mainloop()
