''' Classe Ball
    circle(Surface, color, pos, radius, width=0)
    pass - passa o comando
 '''
import pygame
from pygame.locals import *

class Ball:
    def __init__( self, radius, color,speed = 1 ):
        self.x = 0
        self.y = 0
        self.color = color
        self.radius = radius
        self.width = radius * 2
        self.direction_x = 1 * speed
        self.direction_y = 1 * speed

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
        color = self.color 
        
        pygame.draw.circle( screen, color, self.position, self.radius )    
        
      
