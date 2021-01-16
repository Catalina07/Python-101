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
images = {"logo":pg.image.load("imgs/logo.png"),0:pg.image.load("imgs/empty.png"), 1:pg.image.load("imgs/v1.png"), 2:pg.image.load("imgs/v2.png"),
          3:pg.image.load("imgs/v3.png"),4:pg.image.load("imgs/v4.png"),5:pg.image.load("imgs/v5.png"),6:pg.image.load("imgs/v6.png")}

# Loading sounds to a dicionary
sounds = {"win":pg.mixer.Sound("sound/win.wav"), "lose":pg.mixer.Sound("sound/lose.wav"),
          "click":pg.mixer.Sound("sound/click.wav")}

alphabet = list(string.ascii_uppercase) # Getting all the letters in the latin alphabet

class Button(object): # A GENERAL CLASS FOR ALL THE BUTTONS ON THE SCREEN (LETTERS & LANGUAGE BUTTONS)
    def __init__(self, color, pos, width, height, letter, active = False, type = 1, size = 40):
        self.type = type #TYPE 1 IS A LETTER, TYPE 2 IS A LANGUAGE BUTTON
        self.active = active    # A VARIABLE ONLY FOR TYPE 2
        self.clicked = False    # A VARIABLE ONLY FOR TYPE 1
        self.rollOver = False   # A VARIABLE ONLY FOR TYPE 1
        self.size = size
        self.font = pg.font.SysFont(None, self.size)
        self.color = color
        self.letter = letter
        self.pos = pos
        self.width = width
        self.height = height
        self.subsurface = pg.Surface((self.width, self.height))         # CREATING A SUBSURFACE TO
        self.subsurface.fill(self.color)                                # GET A RECT (FOR COLLISION)
        self.text = self.font.render(self.letter, True, colors["lavender"])

    def Draw(self, surface):
         if self.type == 1:
            if self.rollOver:                   # IF A TYPE 1 BUTTON IS UNDER
                self.subsurface.set_alpha(200)  # THE MOUSE, MAKE IT LESS VIBRANT
            else:
                self.subsurface.set_alpha(255)
            if not self.clicked:
                surface.blit(self.subsurface, self.pos)
                self.subsurface.blit(self.text, (self.width/4,self.height/5))
        if self.type == 2:
            if self.active:                     # IF A TYPE 2 BUTTON IS ACTIVE
                self.subsurface.set_alpha(255)  # MAKE IT'S COLOR MORE VIBRANT
            else:
                self.subsurface.set_alpha(100)
            surface.blit(self.subsurface, self.pos)
            self.subsurface.blit(self.text, (self.width / 4, self.height / 5))



notesArea = pg.Surface((sw,700))        # CREATING TWO
notesArea.fill(colors["lavender"])         # AREAS WITH DIFFERENT
                                        # COLORS
buttonArea = pg.Surface((sw, 100))
buttonArea.fill(colors["lilac"])

letters = []
j = 0   # TO ALIGN THE LETTERS ON THE SCREEN ( VERTICALLY )
for number, letter in enumerate(alphabet):
    if number > 12: # TO ALIGN THE LETTERS ON THE SCREEN ( HORIZONTALLY )
        number = number - 13
        j = 1
    letters.append(Button(colors["gray"], (70+number*90,140+j*60), 50, 50, letter))

languageButtons = []
languageButtons.append(Button(colors["blue"], (30, 400), 85,40, "English", False, 2, 20))
languageButtons.append(Button(colors["blue"], (120, 400), 85,40, "Romana", True, 2, 20))

errorCount = 0

# ROMANIAN WORDS
wordsRO = ["HAIDUCII", "AUTOBRONZANT", "STRAZILE DIN BUCURESTI", "NEBUN DE ALB", "DRAGOSTE DE INCHIRIAT",
            "DE CE PLANG CHITARELE", "NOAPTEA GOLANII"]

# ENGLISH WORDS
wordsEN = ["YOU GIVE LOVE A BAD NAME", "LET IT BE", "HOLD THE LINE", "PIANO MAN", "DANCING QUEEN",
            "NOTHING ELSE MATTERS", "ANOTHER BRICK IN THE WALL", "HOTEL CALIFORNIA", "HYPNOTYZE",
            "AMBITIONZ AZ A RIDAH"]

languageChoice = 1 # 1 == ROMANIAN, 2 == ENGLISH, DEFAULT IS ROMANIAN
if languageChoice == 1:
    currentLanguage = wordsRO
else:
    currentLanguage = wordsEN
currentWord = random.randrange(0, len(currentLanguage))

guessed = []

lw = 40 # WIDTH OF THE LINE FOR THE LETTERS
ls = 10 # SPACE BETWEEN THE LINES

needRestart = False # FOR CONDITIONS IN WHICH YOU NEED TO RESTART THE GAME, LIKE CHANGING THE LANGUAGE
winCount = 0
pointCount = 0
spaceCount = 0  # COUNTING HOW MANY SPACES A WORD HAS, IT'LL BE IMPORTANT WHEN CHECKING-
for letter in currentLanguage[currentWord]: # - IF YOU GUESSED THE WORD COMPLETELY.
    if letter == " ":
        spaceCount += 1
print(len(wordsEN))
print(len(wordsRO))