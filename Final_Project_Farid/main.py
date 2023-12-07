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
    pg.draw.rect(screen, "GRAY", [0, 610, WIDTH, 110])
    pg.draw.rect(screen, "BLACK", [0, 610, WIDTH, 5])
    # Draws a vertical gray rectangle on the left-hand side of the screen, this will hold all of the tools
    pg.draw.rect(screen, "GRAY", [0, 0, 190, 720])
    pg.draw.rect(screen, "BLACK", [190, 0, 5, 610])
    # Start of Color configuration interface
    WHITE = pg.draw.rect(screen, (0, 0, 0), [10, 10, 50, 50])
    BLACK = pg.draw.rect(screen, (255, 255, 255), [10, 70, 50, 50])
    BLUE = pg.draw.rect(screen, (0, 0, 255), [10, 130, 50, 50])
    RED = pg.draw.rect(screen, (255, 0, 0), [70, 10, 50, 50])
    GREEN = pg.draw.rect(screen, (0, 255, 0), [70, 70, 50, 50])
    YELLOW = pg.draw.rect(screen, (255, 255, 0), [70, 130, 50, 50])
    ORANGE = pg.draw.rect(screen, (255, 165, 0), [130, 10, 50, 50])
    PURPLE = pg.draw.rect(screen, (128, 0, 128), [130, 70, 50, 50])
    BROWN = pg.draw.rect(screen, (165, 42, 42), [130, 130, 50, 50])
    ColorList = [WHITE, BLACK, BLUE, RED, GREEN, YELLOW, ORANGE, PURPLE, BROWN]
    RgbList = [(0, 0, 255), (255, 0, 0), (0, 255, 0), (255, 255, 0), (0, 255, 255), (255, 0, 255), (0, 0, 0), (255, 255, 255), (165, 42, 42), (128, 0, 128), (255, 165, 0)]
    # Brush Sizes interface
    XXSb = pg.draw.rect(screen, "BLACK", [10, 250, 50, 50])
    pg.draw.circle(screen, "WHITE", (35, 275), 5)
    XSb = pg.draw.rect(screen, "BLACK", [70, 250, 50, 50])
    pg.draw.circle(screen, "WHITE", (95, 275), 10)
    Sb = pg.draw.rect(screen, "BLACK", [130, 250, 50, 50])
    pg.draw.circle(screen, "WHITE", (155, 275), 15)
    BList = [XXSb, XSb, Sb]

    return BList, ColorList, RgbList




# Game loop
running = True
while running:
    # keep the loop running using teh clock
    clock.tick(FPS)

    for event in pg.event.get():
        # check for lcosed window
        if event.type == pg.QUIT:
            running = False

    # Fills the full screen with white
    screen.fill((0, 0, 0))

    # When the mouse is located on the canvas, based on the configurations, you can draw
    mouse = pg.mouse.get_pos()
    if mouse[1] > 70:
        pg.draw.circle(screen, active_color, mouse, active_size)
    brushes, colors, Rgbs = draw_menu()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

        if event.type == pg.MOUSEBUTTONDOWN:
            for i in range(len(brushes)):
                if brushes[i].collidepoint(event.pos):
                    active_size = 20 - (i * 5)
            
            for i in range(len(colors)):
                if colors[i].collidepoint(event.pos):
                    active_color = Rgbs[i]


    # buffer - after drawing everyhting, flip the display
    pg.display.flip()

pg.quit()
