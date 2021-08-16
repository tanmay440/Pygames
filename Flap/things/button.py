#from .settings import *

import pygame
pygame.init()
def getFont(size):
    return pygame.font.SysFont("algerian", size)

class Button():
    
    
    def __init__(self, x, y, width, height, colour, text = None, text_colour = (0, 0, 0)):
    
    
        self.x = x
    
    
        self.y = y
    
    
        self.width = width
    
    
        self.height = height
    
    
        self.colour = colour
    
    
        self.text = text
    
    
        self.text_colour = text_colour
    
    
    def draw(self, win):
    
    
        pygame.draw.rect(win, self.colour, (self.x, self.y, self.width, self.height))
    

        pygame.draw.rect(win, (0, 0, 0), (self.x, self.y, self.width, self.height), 3)


        if self.text:
        
        
            button_font = getFont(16)
        
        
            text_surface = button_font.render(self.text, 1, self.text_colour)
        
        
            win.blit(text_surface, (self.x, self.y))


    def clicked(self, pos):


        x, y = pos


        if not(x >= self.x and x <= self.x + self.width):


            return False


        if not(y >= self.y and y <= self.y + self.height):



                return False

        
        return True
