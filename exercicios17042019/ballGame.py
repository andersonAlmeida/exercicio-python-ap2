""" Classe BallGame herda de Game """

from game import Game 
import pygame, sys, math
from ball import Ball
from window import Window
from movement import Movement
from pygame.locals import *

class BallGame( Game ):
    def __init__(self, width, height, title):
        super().__init__()

        self.screen = Window(width, height, title)
        self.ball = Ball( 20, (0, 0, 255) , 2 )
        self.ball.position = ( math.ceil(width/2), math.ceil(height/2) )

        self.movementObj = Movement( self.ball.x, self.ball.y, self.ball.radius )

        self.speed = 1

        self.createObjects([ self.ball ])
        self.run()
        

    def run(self):
        pygame.init()
        pygame.key.set_repeat(1, 1) #enable held key event

        self.screen.createWindow()
        running = True
        angle = 0

        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                    pygame.quit()
                    sys.exit(0) 

            if angle < 359:
                angle += 0.05
            else:
                angle = 0        

            self.ball.x, self.ball.y = self.movementObj.move(self.ball.x, self.ball.y, angle, 5)  
            
            # print(self.ball.direction_x, self.ball.direction_y)    

            # self.ball.move( self.ball.x, self.ball.y )

            self.update()            
            self.draw()        

            

game = BallGame(1024, 600, 'Oi sou o PyGame')