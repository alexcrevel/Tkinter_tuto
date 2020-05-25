from tkinter import *
from random import randrange

NB_IMG=8
SIDE=100
WIDTH=SIDE*NB_IMG
X0=Y0=SIDE//2

root = Tk()
logo = PhotoImage(file="python.gif")
cnv = Canvas(root, width=WIDTH, height=SIDE, bg="ivory")
cnv.pack(pady=100)

ids=[]
for k in range(NB_IMG):
    id_image=cnv.create_image(X0+k*SIDE, Y0, image=logo)
    ids.append(id_image)

j=randrange(NB_IMG)
print(j)
mon_id=ids[j]

cnv.delete(mon_id)

root.mainloop()  
