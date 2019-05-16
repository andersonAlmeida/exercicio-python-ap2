class Ponto:
    def __init__(self, x, y):
        self.__x = x #protegido
        self.__y = y #protegido

    @property #getter
    def x(self):
        return self.__x
    
    @property #getter
    def y(self):
        return self.__y

    def distance(self, ponto):
        cx = self.__x - ponto.x
        cy = self.__y - ponto.y

        return (cx*cx + cy*cy) ** 0.5
