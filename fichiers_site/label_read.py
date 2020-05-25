from tkinter import *

root=Tk()
lbl=Label(root,text="42", font="courier 20 bold")
lbl.pack(padx=50, pady=50)

print(lbl['text'])

root.mainloop() 
