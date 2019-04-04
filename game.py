""" Classe Window  """

import pygame, sys
from ball import Ball
from window import Window
from pygame.locals import *

class Game:
    def __init__(self):
        self.screen = Window(800, 600, 'Oi, sou o PyGame.')
        self.ball = Ball( 20 )
        self.ball.position = (400, 300)

        self.run()

    def draw(self):
        self.screen.draw( self.ball )
    
    def update(self):
        self.screen.update()
        pygame.time.Clock().tick(240)

    @property 
    def window(self):
        pass
    
    @window.setter
    def size(self, size):
        pass

    def add_object(self, obj):
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
            
            self.draw()
            self.update()            

# game = Game()