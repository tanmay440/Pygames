from items.PlayerControler import Player
import items
import pygame
from pygame.constants import K_t
import random
with  open("text.txt", "w") as t:
    pass
hi = pygame.init()
screen=pygame.display.set_mode([1200, 500])
screen.fill([0, 0, 0])
run = True
link = pygame.image.load("e:/Pgames/doje/assets/player.png")
enemy = pygame.image.load("E:\\Pgames\\doje\\assets\\sprite_0.png")
pos = [0, 300, 600, 900]
y = 1200
k = items.Player(600, 420, 64, 32, 5, 500, 1200, screen, link)
while run:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run = False
        k.draw()
        k.move()
        if y == 1200:
            y = 0
            with  open("text.txt", "w") as t:
                pass
        
            for x in random.sample(pos, 3):
                screen.blit(enemy, (x, y))
                with open("text.txt", "a") as t:
                    t.write(str(x) + "\n")
        y += 1
        screen.fill([0, 0, 0])
        with  open("text.txt") as t:
            x=t.read().split("\n")
            del x[-1]
        for z in x:
            screen.blit(enemy, [int(z), y])
pygame.quit()