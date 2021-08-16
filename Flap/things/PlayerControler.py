import pygame
from pygame.constants import K_t
pygame.init()
class Player():
    def __init__(self, accleration, stsrt_x, stsrt_y, col, screen, x_scale, y_scale, gravity, screen_height, screen_width,  sprite):
        '''
        A class for a player who can not fly or swim but can walk and jump
        '''
        self.accleration = accleration
        self.start_x = stsrt_x
        self.start_y = stsrt_y
        self.col = col
        self.screen = screen
        self.x_scale = x_scale
        self.y_scale = y_scale
        self.g = gravity
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.sprite = sprite
        self.facing = "idle"
        

    def draw(self):
        pygame.draw.rect(self.screen, self.col, [self.start_x, self.start_y, self.x_scale, self.y_scale], 0)
        
        self.screen.blit(self.sprite, (self.start_x, self.start_y))
        pygame.display.flip()
    def move(self, gh = 0):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and self.start_y > self.g:
            self.start_y -= self.g * 0.5
            self.facing = "up"
        elif self.start_y < self.screen_height - self.x_scale - self.g - gh:
            self.start_y += self.g
            self.facing = "idle"
        if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and self.start_x > self.accleration:
            self.start_x -= self.accleration
            if not(keys[pygame.K_UP] or keys[pygame.K_w]):
                self.facing = "left"
        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and self.start_x < self.screen_width - self.x_scale - self.accleration:
            self.start_x += self.accleration
            if not(keys[pygame.K_UP] or keys[pygame.K_w]):
                self.facing = "right"
        self.player = pygame.Rect((self.start_x, self.start_y, self.x_scale, self.y_scale))

if __name__ == "__main__":
    screen=pygame.display.set_mode([1200, 500])
    screen.fill([0, 0, 0])
    link = pygame.image.load("E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket0.png")
    t = Player(2, 100, 100, (255, 0, 0), screen, 160, 160, 2, 500, 1200,  link)
    t.draw()    
    run = True
    anim = ["E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket0.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket0.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket0.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket1.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket1.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket1.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket2.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket2.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket2.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket3.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket3.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket3.png"]
    i = 0
    clock = pygame.time.Clock()
    while run:
        clock.tick(27)
        if t.facing == "idle":
            anim = ["E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket_idle0.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket_idle0.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket_idle0.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket_idle0.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket_idle0.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket_idle0.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket_idle0.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket_idle0.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket_idle0.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket_idle0.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket_idle0.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket_idle0.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket_idle0.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket_idle1.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket_idle1.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket_idle1.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket_idle1.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket_idle1.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket_idle1.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket_idle1.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket_idle1.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket_idle1.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket_idle1.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket_idle1.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket_idle1.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket_idle1.png", ]
        elif t.facing == "up":
            anim = anim = ["E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket0.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket0.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket0.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket1.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket1.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket1.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket2.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket2.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket2.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket3.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket3.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket3.png"]
        elif t.facing == "left":
            anim = anim = ["E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket_left0.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket_left0.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket_left0.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket_left1.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket_left1.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket_left1.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket_left2.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket_left2.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket_left2.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket_left3.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket_left3.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket_left3.png"]
        elif t.facing == "right":
            anim = anim = ["E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket_right0.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket_right0.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket_right0.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket_right1.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket_right1.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket_right1.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket_right2.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket_right2.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket_right2.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket_right3.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket_right3.png", "E:/Assets/Pygame scripts/Player/Cannot Fly/Cannot swim/rocket_right3.png"]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if i >= len(anim):
            i = 0
        t = Player(18, t.start_x, t.start_y, (0, 0, 255), screen, 180, 160, 18, 500, 1200, pygame.image.load(anim[i]))        
        t.move()
        t.draw()
        keys = pygame.key.get_pressed()
        screen.fill([0, 0, 0])
        i += 1
        
