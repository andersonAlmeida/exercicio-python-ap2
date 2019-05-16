class Circle:
    def __init__(self, centro, raio):
        self.__centro = centro
        self.__raio = raio
    
    @property
    def ray(self):
        return self.__raio
    
    @property
    def center(self):
        return self.__centro

    def hit_point(self, ponto):
        return self.__centro.distance(ponto) <= self.__raio

    def hit_circle(self, circle):
        dmax = self.__raio + circle.ray
        d = self.__centro.distance(circle.center)
        return d <= dmax