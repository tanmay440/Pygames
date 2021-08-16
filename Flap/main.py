import pygame
from things import *
import random
pygame.init()
win = pygame.display.set_mode((1100, 650))
link = pygame.image.load("E:/Pgames/Flap/assets/sprite_0.png")
k = Player(25, 0, 150, (255//1, 255//2, 255//4), win, 64, 64, 25, 650, 1100, link)
bean = [pygame.image.load("e:/Pgames/Flap/assets/sprit0.png"), random.randint(0, 1050), random.randint(0, 575), False]
beans = [[pygame.image.load("e:/Pgames/Flap/assets/sprit0.png"), random.randint(0, 1050), random.randint(0, 575), False], [pygame.image.load("e:/Pgames/Flap/assets/sprit0.png"), random.randint(0, 1050), random.randint(0, 575), False], [pygame.image.load("e:/Pgames/Flap/assets/sprit0.png"), random.randint(0, 1050), random.randint(0, 575), False]]
run = True
clock = pygame.time.Clock()
def make_current_round(round_no):
    while  len(beans) < round_no+2:
        beans.append([pygame.image.load("e:/Pgames/Flap/assets/sprit0.png"), random.randint(0, 1050), random.randint(0, 650), False])
def is_all_clear(beans):
    for x in beans:
        if x[3] == False:
            return False
    return True
'''
def is_collide(py, ph, px, pw, by, bh, bx, bw):
    if py - ph < by + bh and py + ph > by:
        if px + pw > bx and px - pw < bx + bw:
            return True
    return False
'''
cl = 1
while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    win.fill([255, 229, 180])
    i = 0
    while i < len(beans) :
        '''if is_collide(k.start_y, k.y_scale, k.start_x, k.x_scale, bean[i][1], 16, bean[i][2], 16):
            bean[i][3] = True'''
        if beans[i][3] == False:
            win.blit(beans[i][0], (beans[i][1], beans[i][2]))
        i += 1
    i = 0
    if is_all_clear(beans):
        cl += 1
    #cl+=2
    make_current_round(cl)
    win.blit(pygame.image.load("e:/Pgames/Flap/assets/s0.png"), (0, 600))
    k.draw()
    k.move(50)
    