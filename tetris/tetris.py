import pygame, sys
from enum import Enum
from pygame.locals import *

pygame.init()

#colors needed for the blocks
RED = (255,0,0)
BLUE = (0,0,255)
ORANGE = (255,165,0)
PINK = (255,192,203)
CYAN = (0,255,255)
GREEN = (0,255,0)
YELLOW = (255,255,0)
BACKGROUND = (0,0,0)

#the size of each individual square on the board in pixels
blocksize = 20

#the board for the blöcks 
board = [[RED,BLUE,ORANGE,PINK,CYAN,GREEN,YELLOW,RED,BLUE,ORANGE] for _ in range(40)]

def draw_board(screen):
    for y in range(40):
        for x in range(10):
            pygame.draw.rect(screen,board[y][x],(x*blocksize,y*blocksize,blocksize,blocksize))


FPS = 30
FramePerSec = pygame.time.Clock()

(width,height) = (200,800)
DISPLAYSURF = pygame.display.set_mode((width,height))
DISPLAYSURF.fill(BACKGROUND)
pygame.display.set_caption('Tetris')

while True:
    draw_board(DISPLAYSURF)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
   
    FramePerSec.tick(FPS)

class Pice:
    def __init__ (self, shape, color, x, y):
        self.c = color
        self.s = shape
        self.x = x
        self.y = y

#class Board: