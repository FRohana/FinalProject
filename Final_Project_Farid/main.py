# Cites:
# https://www.youtube.com/watch?v=h2uRcZUfyqM&ab_channel=LeMasterTech
# 

'''
Software: PyPaint

Goals:
- Multiple paint tools
- Erasing tools
- An interafce for the user
- Possibly cropping tools
- Reset canvas tool

'''



import pygame as pg
import random
from settings import *

pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT,))
pg.display.set_caption("My Game")
clock = pg.time.Clock()

# This function draws the items and shapes required for the interface of the programm
def draw_menu():
    # Draws a horizontal gray line on the top of the screen, this will hold color options
    pg.draw.rect(screen, "gray", [0, 0, WIDTH, 110])
    pg.draw.rect(screen, "black", [0, 110, WIDTH, 5])
    # Draws a vertical gray rectangle on the left-hand side of the screen, this will hold all of the tools
    pg.draw.rect(screen, "gray", [0, 0, 180, 720])
    pg.draw.rect(screen, "black", [180, 110, 5, 610])



# Game loop
running = True
while running:
    # keep the loop running using teh clock
    clock.tick(FPS)

    for event in pg.event.get():
        # check for lcosed window
        if event.type == pg.QUIT:
            running = False

    # Update

    # Draw
    screen.fill(WHITE)

    draw_menu()
    # buffer - after drawing everyhting, flip the display
    pg.display.flip()

pg.quit()
