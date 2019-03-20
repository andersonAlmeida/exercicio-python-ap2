import pygame, sys
from pygame.locals import *

class Window:
    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.title = title

    def openWindow(self):
        DISPLAYSURF  = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption( self.title )
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()

    def start(self):
        pygame.init()
        self.openWindow()



screen = Window(800, 600, 'Oi, sou o PyGame.')

screen.start()