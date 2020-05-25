from tkinter import *
import pygame

pygame.mixer.init()

mon_audio=pygame.mixer.Sound("clap.wav")

def lancer():
    mon_audio.play(-1)
    
def couper():
    mon_audio.stop()

fen = Tk()

Button(fen,text="Son",command=lancer, width=40).pack(pady=20)
Button(fen,text="Couper",command=couper, width=40).pack(pady=20)

fen.mainloop() 
