''' Classe Ball
    circle(Surface, color, pos, radius, width=0)
    pass - passa o comando
 '''
import pygame
from pygame.locals import *

class Ball:
    def __init__( self, radius ):
        self.x = 0
        self.y = 0
        self.radius = radius
        self.width = radius * 2
        self.direction_x = 1
        self.direction_y = 1

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

        if self.collisionDetection(screen):
            self.direction_x *= -1
            self.direction_y *= -1            

        self.move(self.direction_x, self.direction_y)
        
        pygame.draw.circle( screen, color, self.position, self.radius )
    
    def collisionDetection(self, screen):
        hasCollision = False

        if self.x + self.radius >= screen.get_width() or self.x - self.radius <= 0: # x collision
            hasCollision = True

        if self.y + self.radius >= screen.get_height() or self.y - self.radius <= 0: # y collision
            hasCollision = True

        return hasCollision   
