from tkinter import *
import pygame

pygame.mixer.init()

mon_audio=pygame.mixer.Sound("clap.wav")


def lancer():
    mon_audio.set_volume(1)
    mon_audio.play(3)
    
def couper():
    mon_audio.stop()

def quitter():
    pygame.quit()
    fen.destroy()

fen = Tk()

Button(fen,text="Son",command=lancer, width=40).pack(pady=20)
Button(fen,text="Couper",command=couper, width=40).pack(pady=20)
fen.protocol("WM_DELETE_WINDOW", quitter)

fen.mainloop() 
