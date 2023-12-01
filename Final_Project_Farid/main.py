
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
    screen.fill(BLACK)

    # buffer - after drawing everyhting, flip the display
    pg.display.flip()

pg.quit()
