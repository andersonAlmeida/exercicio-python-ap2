""" Classe BallGame herda de Game """

from game import Game 
import pygame, sys
from ball import Ball
from window import Window
from player import Player
from pygame.locals import *

class BallGame( Game ):
    def __init__(self, width, height, title):
        super().__init__()

        self.screen = Window(width, height, title)
        self.ball = Ball( 10 )
        self.ball.position = (400, 300)
        self.player1 = Player(25, 100, 0, (self.screen.height / 2) - 50 )
        self.player2 = Player(25, 100, 775, (self.screen.height / 2) - 50 )

        self.createObjects([ self.ball, self.player1, self.player2 ])
        self.run()

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
            
            if self.collisionDetectionX(self.screen):
                self.ball.direction_x *= 1

            self.update()            
            self.draw()

    def collisionDetectionX(self, screen):
        hasCollision = False

        if self.ball.x + self.ball.radius >= self.player2.x or self.ball.x - self.ball.radius <= self.player1.x: # x collision
            hasCollision = True

        return hasCollision   

            

game = BallGame(800, 600, 'Oi sou o PyGame')