''' Classe Bola
    circle(Surface, color, pos, radius, width=0)
    pass - passa o comando
 '''
import pygame
from pygame.locals import *

class Bola:
    def __init__( self, radius ):
        self.x = 0
        self.y = 0
        self.radius = radius

    @property
    def position(self):
        return (self.x, self.y)

    @position.setter
    def position(self, position):
        self.x, self.y = position

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def draw(self, screen):
        color = (255, 255, 255)
        self.move(1, 1)
        pygame.draw.circle( screen, color, self.position, self.radius )