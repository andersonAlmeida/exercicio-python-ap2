''' Classe Player '''
import pygame
from pygame.locals import *

class Player():
    def __init__(self, width, height, pos_x, pos_y):
        self.x = pos_x
        self.y = pos_y
        self.width = width
        self.height = height

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
        
        # self.move(self.direction_x, self.direction_y)
        
        pygame.draw.rect( screen, color, pygame.Rect(self.x, self.y, self.width, self.height) )