import pygame as pg
import numpy as np
import random
import string
import sys
pg.mixer.pre_init(44100, -16, 1, 512) # TO REDUCE SOUND DELAY
pg.init()

sw,sh = 1280, 760 # ScreenWidth, ScreenHeight
sc = (sw/2, sh/2) # Shortcut for the center of the screen
screen = pg.display.set_mode((sw,sh))
pg.display.set_caption("Hangman python101")
default_font = pg.font.SysFont(None, 40)


# Assigning all the primary/secondary colors to a dictionary to use more practically
colors = {"black":(0,0,0), "darkgray":(70,70,70), "gray":(128,128,128), "lightgray":(200,200,200), "white":(255,255,255), "red":(255,0,0),
          "darkred":(128,0,0),"green":(0,255,0),"darkgreen":(0,128,0), "blue":(0,0,255), "navy":(0,0,128), "darkblue":(0,0,128),
          "yellow":(255,255,0), "gold":(255,215,0), "orange":(255,165,0), "lilac":(229,204,255),"lightblue":(135,206,250),"teal":(0,128,128),
          "cyan":(0,255,255), "purple":(150,0,150), "pink":(238,130,238), "brown":(139,69,19), "lightbrown":(222,184,135),"lightgreen":(144,238,144),
          "turquoise":(64,224,208),"beige":(245,245,220),"honeydew":(240,255,240),"lavender":(230,230,250),"crimson":(220,20,60)}

# Loading images to a dictionary
# images = {"logo":pg.image.load("imgs/logo.png"),0:pg.image.load("imgs/empty.png"), 1:pg.image.load("imgs/v1.png"), 2:pg.image.load("imgs/v2.png"),
#           3:pg.image.load("imgs/v3.png"),4:pg.image.load("imgs/v4.png"),5:pg.image.load("imgs/v5.png"),6:pg.image.load("imgs/v6.png")}

# # Loading sounds to a dicionary
# sounds = {"win":pg.mixer.Sound("sound/win.wav"), "lose":pg.mixer.Sound("sound/lose.wav"),
#           "click":pg.mixer.Sound("sound/click.wav")}

alphabet = list(string.ascii_uppercase) # Getting all the letters in the latin alphabet

class Button(object): # A GENERAL CLASS FOR ALL THE BUTTONS ON THE SCREEN (LETTERS & LANGUAGE BUTTONS)
    def __init__(self, color, pos, width, height, letter, active = False, type = 1, size = 40):
        pass

    def Draw(self, surface):
        pass