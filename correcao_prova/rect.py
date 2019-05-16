class Rect:
    def __init__(self, x, y, w, h):
        self.__x = x
        self.__y = y
        self.__w = w
        self.__h = h

    def bounds(self):
        return (self.__x, self.__y, self.__w, self.__h)

    
    def dimension(self):
        return (self.__w, self.__h)


    def center(self):
        return (self.__x + self.__w / 2.0, self.__y + self.__h / 2.0)


    def hit_point(self, point):
        x, y = point.x, point.y
        
        if x < self.__x or x > self.__w:
            return False
        
        if y < self.__y or y > self.__h:
            return False
        
        return True


    def hit_rect(self, x, y, w, h):
        ponto1 = (x, y)
        ponto2 = (x+w, y)
        ponto3 = (x+w, y+h)
        ponto4 = (x, y+h)

        if( self.hit_point( ponto1 ) ):
            return False
        
        if( self.hit_point( ponto2 ) ):
            return False

        if( self.hit_point( ponto3 ) ):
            return False
        
        if( self.hit_point( ponto4 ) ):
            return False
        
        return True

    
    # def hit_circle(self, point, rad):



r = Rect(0, 0, 100, 30 )

if r.hit_rect(5, 5, 200, 20):
    print('Está dentro')
else:
    print('Está fora')


        