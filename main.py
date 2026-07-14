import pygame as pg
from pygame.locals import *

# constants
WIDTH, HEIGHT = 1280, 720
# setup
pg.init()

# window
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Pool")

# clock
clock = pg.time.Clock()

# game loop
start = False
running = True
while running:
    # event loop
    for event in pg.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

    screen.fill("black")

    # UPDATE
    keys = pg.key.get_pressed()

    # DRAW

    pg.display.flip()

    # fps cap
    clock.tick(60)

pg.quit()
