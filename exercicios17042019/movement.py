''' class Movement '''
import math

class Movement:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
    
    def move(self, x, y, angle, radius):

        px = int( x + math.cos(angle) * radius )
        py = int( y + math.sin(angle) * radius )
    
        return (px, py)


