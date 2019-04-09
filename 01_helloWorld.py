'''
title: Hello World
author: garrett
date created: 2019-04-08
'''

import pygame
pygame.init() # loads pygame module commands in the program

# Display Variables
TITLE = 'Hello World' # Appears in the window title
FPS = 30 # fps
WIDTH = 800
HEIGHT = 600
SCREENDIM = (WIDTH, HEIGHT)

# Color Variables
WHITE = (255,255,255)
BLACK = (0,0,0)
GREY = (50,50,50)
YELLOW = (255,255,0)
# Create the Window

screen = pygame.display.set_mode(SCREENDIM) # Creates the main surface where all other assets are placed on top
pygame.display.set_caption(TITLE) # This update the window title with TITLE
screen.fill(GREY) # Fills the entire surface with the color. Think of fill as erase

clock = pygame.time.Clock() # Starts a clock to measure time

## Add text
class text:
    def __init__(self, text = 'hello world', pos = (0,0)):
        self.text = text
        self.color = (255,255,255)
        self.size = 28
        self.x = pos[0]
        self.y = pos[1]
        self.pos = (self.x, self.y)
        self.fontFam = 'Arial'
        self.font = pygame.font.SysFont(self.fontFam, self.size)
        self.surface = self.font.render(self.text, 1, self.color)

    def getText(self):
        return self.surface

    def getPOS(self):
        return self.pos

    def setColor(self, color):
        self.color = color
        self.surface = self.font.render(self.text, 1, self.color)

    def setSize(self, size):
        self.size = size
        self.font = pygame.font.SysFont(self.fontFam, self.size)
        self. surface = self.font.render(self.text, 1, self.color)

    def setPOS(self, x, y):
        self.x = x
        self.y = y
        self.pos = (self.x, self.y)
        self.surface = self.font.render(self.text, 1, self.color)

    def setFont(self, font):
        self.fontFam = str(font)
        self.font = pygame.font.SysFont(self.fontFam, self.size)
        self.surface = self.font.render(self.text, 1, self.color)

    def moveText(self):
        self.x += 15
        self.pos = (self.x, self.y)
        screen.blit(self.getText(), self.getPOS())
        

# --- CODE STARTS HERE --- #

myText = text('Hello', (100,100))
myText.setColor(YELLOW)
myText.setSize(100)
myText.setPOS(20,10)
myText.setFont('Times New Roman')

newText = text('world')
newText1 = text('a',(30,20))
newText2 = text('b',(50,90))
newText3 = text('c', (200, 100))
running = True
while running:
    for event in pygame.event.get(): # returns all inputs and triggers into an array
        if event.type == pygame.QUIT: # If the red X was clicked.
            running = False
    myText.moveText()
    screen.blit(myText.getText(), myText.getPOS())
    screen.blit(newText.getText(), newText.getPOS())
    screen.blit(newText1.getText(), newText1.getPOS())
    screen.blit(newText2.getText(), newText2.getPOS())
    screen.blit(newText3.getText(), newText3.getPOS())
    clock.tick(FPS) # pause the game until the FPS time is reached
    pygame.display.flip() # update the screen with changes.

pygame.quit()