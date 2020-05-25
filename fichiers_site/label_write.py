from tkinter import *

root=Tk()
lbl=Label(root,text=42, font="courier 20 bold")
lbl.pack(padx=50, pady=50)

def changer():
    lbl['text']=2020

root.after(2000, changer)

root.mainloop()
