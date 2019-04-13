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
            
            self.collisionDetection(self.screen)
            # if self.collisionDetection(self.screen):
                # self.ball.direction_x *= -1

            self.update()            
            self.draw()

    def collisionDetection(self, screen):
        # hasCollision = False
        bx = self.ball.x #ball position x
        by = self.ball.y #ball position Y
        br = self.ball.radius # ball radius
        # bDirectionX = self.ball.direction_x
        # bDirectionY = self.ball.direction_y

        p1x = self.player1.x #player 1 position x
        p1y = self.player1.y #player 1 position y
        p1width = self.player1.width #player 1 width
        p1height = self.player1.height #player 1 height

        p2x = self.player2.x #player 2 position x
        p2y = self.player2.y #player 2 position y
        # p2width = self.player2.width #player 2 width
        p2height = self.player2.height #player 2 height

        #bounds collision
        if by - br <= 0 or by + br >= screen.height:
            self.ball.direction_y *= -1

        # ball collision against player 1
        if bx - br <= p1x + p1width and by + br >= p1y and by - br <= p1y + p1height:
            self.ball.direction_x *= -1

        # ball collision against player 2
        if bx + br >= p2x and by + br >= p2y and by - br <= p2y + p2height:
            self.ball.direction_x *= -1

        

            

game = BallGame(800, 600, 'Oi sou o PyGame')