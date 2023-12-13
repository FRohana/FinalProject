# Cites:
# https://www.youtube.com/watch?v=h2uRcZUfyqM&ab_channel=LeMasterTech
# https://www.cleanpng.com/png-reset-button-computer-icons-clip-art-restart-828846/

'''
Software: PyPaint

Goals:
- Multiple paint tools
- Erasing tools
- An interafce for the user
- Possibly cropping tools
- Reset canvas tool

'''


# settings 
WIDTH = 1280
HEIGHT = 720
FPS = 60
active_size = 0
active_color = "black"
painting = []

# user settings
PLAYER_JUMP = 23
PLAYER_GRAV = 1.5
global PLAYER_FRIC
PLAYER_FRIC = 0.2



import pygame as pg
import random
from settings import *
import os
from pygame.sprite import Sprite


game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')

pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("PyPaint")
clock = pg.time.Clock()




# Interface

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
    RgbList = [(0, 0, 0), (255, 255, 255), (0, 0, 255), (255, 0, 0), (0, 255, 0), (255, 255, 0), (255, 165, 0), (128, 0, 128), (165, 42, 42)]
    # Brush Sizes interface
    XXSb = pg.draw.rect(screen, "BLACK", [10, 250, 50, 50])
    pg.draw.circle(screen, "WHITE", (35, 275), 5)
    XSb = pg.draw.rect(screen, "BLACK", [70, 250, 50, 50])
    pg.draw.circle(screen, "WHITE", (95, 275), 10)
    Sb = pg.draw.rect(screen, "BLACK", [130, 250, 50, 50])
    pg.draw.circle(screen, "WHITE", (155, 275), 15)
    BList = [Sb, XSb, XXSb]


    return BList, ColorList, RgbList


# Eraser Class

class Eraser(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(img_folder, 'reset1.png')).convert()
        self.image.fill((255, 255, 255))  # Set the color of the eraser (white in this case)
        self.rect = self.image.get_rect()
        self.rect.center = (100, 400)


    

# Creates a group for all sprites
all_sprites = pg.sprite.Group()

# make the Eraser class
Eraser = Eraser()

# adds eraser to all sprites group
all_sprites.add(Eraser)



def draw_painting(paints):
    for i in range(len(paints)):
        pg.draw.circle(screen, paints[i][0], paints[i][1], paints[i][2])


# Game loop
running = True
while running:
    # keep the loop running using the clock
    clock.tick(FPS)

    for event in pg.event.get():
        # check for closed window
        if event.type == pg.QUIT:
            running = False


    if event.type == pg.MOUSEBUTTONDOWN:
            # Checks if the left mouse button is clicked
            if event.button == 1:
                # Check if the eraser tool is selected
                if Eraser.rect.collidepoint(event.pos):
                    painting = []  # Clear the painting when using the eraser
                else:
                    # Check for brush and color selection as before
                    for i in range(len(brushes)):
                        if brushes[i].collidepoint(event.pos):
                            active_size = 20 - (i * 5)
                    
                    for i in range(len(colors)):
                        if colors[i].collidepoint(event.pos):
                            active_color = Rgbs[i]

        
    # Fills the full screen with white
    screen.fill((255, 255, 255))

    # When the mouse is located on the canvas, based on the configurations, you can draw
    mouse = pg.mouse.get_pos()
    left_click = pg.mouse.get_pressed()[0]
    if mouse[1] > 1:
        pg.draw.circle(screen, active_color, mouse, active_size)
    if left_click and mouse[1] > 1:
        painting.append((active_color, mouse, active_size))
    draw_painting(painting)
    brushes, colors, Rgbs = draw_menu()


    # Updates all sprites 
    all_sprites.update()


    # draws all sprites
    all_sprites.draw(screen)

    # after drawing everything, flips the display
    pg.display.flip()

pg.quit()
