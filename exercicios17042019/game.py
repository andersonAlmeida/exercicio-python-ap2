""" Classe Window  """

import pygame, sys
# from ball import Ball
# from window import Window
# from player import Player
from pygame.locals import *

class Game:
    def __init__(self):
        self.objects = []  
        self.screen = 0      

    def createObjects(self, objects):
        self.objects = objects

    def draw(self):        
        self.screen.draw( self.objects )        
    
    def update(self):
        self.screen.update()
        pygame.time.Clock().tick(30)

    @property 
    def window(self):
        return self.screen
    
    @window.setter
    def size(self, size):
        pass
    
    def run(self):
        pygame.init()
        self.screen.createWindow()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                    pygame.quit()
                    sys.exit(0)                  
            
            self.update()            
            self.draw()

# game = Game()