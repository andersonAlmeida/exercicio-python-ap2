""" Classe Window  """

import pygame, sys
from bola import Bola
from janela import Window
from pygame.locals import *

class App:
    def __init__(self):
        pass    

    def start(self):
        pygame.init()
        screen.createWindow()

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()                  
            
            screen.draw( bola )
            screen.update()


screen = Window(800, 600, 'Oi, sou o PyGame.')
bola = Bola( 20 )
bola.position = (400, 300)
game = App()

game.start()