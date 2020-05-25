from tkinter import *

SIDE=400
root = Tk()
cnv = Canvas(root, width=SIDE, height=SIDE, bg='ivory')
cnv.pack()

btn=Button(root, text="Nouveau")
btn.pack()

root.mainloop()
