""" Classe Window  """

import pygame, sys
from pygame.locals import *

class Window:
    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.title = title
        self.screen = 0

    def createWindow(self):
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption( self.title )        

    def update(self):
        pygame.display.update()
    
    def draw(self, obj):
        self.screen.fill( (0,0,0) ) 
        obj.draw( self.screen )
