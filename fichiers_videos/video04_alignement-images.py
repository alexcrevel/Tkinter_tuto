from tkinter import *
# 1. nombre d'images
repet=6
# 2. dimension image
DIM=100
# 3. Ajuster
LARG=repet*DIM
HAUT=DIM

fen=Tk()
cnv=Canvas(fen, width=LARG, height=HAUT, background='ivory')
cnv.pack(pady=20)


logo=PhotoImage(file='python.gif')

# 4. Centre image 1
X0=DIM/2
Y0=DIM/2


# 5. centre image
for i in range(repet):
    centre=(X0+i*DIM, Y0)
    id_image=cnv.create_image(centre, image=logo)
    print(id_image)

fen.mainloop() 
