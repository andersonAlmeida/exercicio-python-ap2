class Fila:
    def __init__(self, size=100):
        self.queue = [None] * size
        self.size = size
        self.tail = 0
        self.head = 0

    def enqueue(self, v):
        prox = self.next( self.tail, self.size )   

        if prox == self.head:
            print("Fila cheia")
            return False

        self.queue[self.tail] = v
        self.tail = prox  

    def dequeue(self):
        if self.empty():
            print("Fila vazia")
            return False

        prox = self.next( self.head, self.size )       

        retorno = self.queue[self.head]
        self.head = prox  

        return retorno

    def peek(self):
        return self.queue[ self.head ]

    def empty(self):
        return self.tail == self.head
    
    def next(self, indice, tam):
        return (indice + 1) % tam