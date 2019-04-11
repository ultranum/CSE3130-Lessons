'''
title: Boxes
author: garrett
date created: 2019-04-08
'''

import pygame
pygame.init() # loads pygame module commands in the program

# Display Variables
TITLE = 'Boxes' # Appears in the window title
FPS = 30 # fps
WIDTH = 800
HEIGHT = 600
SCREENDIM = (WIDTH, HEIGHT)

# Color Variables
WHITE = (255,255,255)
BLACK = (0,0,0)
GREY = (50,50,50)

# Classes
class box:
    def __init__(self, width, height, color = WHITE, x = 0, y = 0):
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        self.color = color
        self.dim = (self.width, self.height)
        self.pos = (self.x, self.y)
        self.surface = pygame.Surface(self.dim, pygame.SRCALPHA, 32)
        self.surface.fill(self.color)
        self.xDir = 1
        self.yDir = 1

    def getBox(self):
        return self.surface

    def getPos(self):
        return self.pos

    def setPos(self, x, y):
        self.x = x
        self.y = y
        self.pos = (self.x, self.y)
        self.surface = pygame.Surface(self.dim, pygame.SRCALPHA, 32)
        self.surface.fill(self.color)

    def setDim(self, width, height):
        self.height = height
        self.width = width
        self.dim = (self.width, self.height)
        self.surface = pygame.Surface(self.dim, pygame.SRCALPHA, 32)
        self.surface.fill(self.color)

    def setColor(self, color):
        self.color = color
        self.surface.fill(self.color)

    def moveBox(self, spdx = 0, spdy = 0):
        self.x += self.xDir*spdx
        self.y += self.yDir*spdy
        self.pos = (self.x, self.y)
        if self.x > WIDTH - self.surface.get_width():
            self.xDir = -1
        elif self.x < 0:
            self.xDir = 1
        if self.y > HEIGHT - self.surface.get_height():
            self.yDir = -1
        elif self.y < 0:
            self.yDir = 1
# Create the Window

screen = pygame.display.set_mode(SCREENDIM) # Creates the main surface where all other assets are placed on top
pygame.display.set_caption(TITLE) # This update the window title with TITLE
screen.fill(GREY) # Fills the entire surface with the color. Think of fill as erase

clock = pygame.time.Clock() # Starts a clock to measure time

# --- CODE STARTS HERE --- #

whitebox = box(50,100)
whitebox.setDim(50,50)
whitebox.setPos(WIDTH/2 - whitebox.getBox().get_width(), HEIGHT/2 - whitebox.getBox().get_width())

running = True
while running:
    for event in pygame.event.get(): # returns all inputs and triggers into an array
        if event.type == pygame.QUIT: # If the red X was clicked.
            running = False
    whitebox.moveBox(10, 10)
    screen.fill(GREY)
    screen.blit(whitebox.surface, whitebox.pos)
    clock.tick(FPS) # pause the game until the FPS time is reached
    pygame.display.flip() # update the screen with changes.
pygame.quit()