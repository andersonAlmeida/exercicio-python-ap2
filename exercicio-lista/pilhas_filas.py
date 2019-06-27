# FILAS - FIFO
# array usado para filas
# nunca usar lista em python para implementar filas, porque é ineficiente pois é um vetor
# formula para achar o próximo tail. T = ( T+1 ) % S
# T: tail
# S: tamanho do array
# enqueue(dado)
# dequeue():dado
# peek():dado - olha qual o próximo elemento
# empty():boolean - testa se está vazia

# PILHAS - LIFO
# Autômato c/ pilha.
# Autômato c/ 2 pilhas resolve qualquer problema computacional. Simula a máquina de Turing.
# Utilidades
# avaliação de expressão aritmética. 235+*
# inversão de expressão aritmética. 2*(3+5) -> 235+*
# validação tag HTML (abrir / fechar)
# push(dado)
# pop():dado
# peek():dado - olha qual o próximo elemento
# empty():boolean - testa se está vazia

class Fila:
    def __init__(self, size):
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

def verFila():
    fila = Fila(8)

    fila.enqueue(1)
    fila.enqueue(2)
    fila.enqueue(3)
    fila.enqueue(4)
    fila.enqueue(5)
    fila.enqueue(6)
    fila.enqueue(7)
    # fila.enqueue(8)

    dq = fila.dequeue()

    while dq is not False:
        if dq:
            print( dq )
            
        dq = fila.dequeue()

    print( fila.peek() )



class Pilha:
    def __init__(self, size):
        self.stack = [None] * size 
        self.topo = -1
        

    def push(self, v):        
        if self.topo == len(self.stack):
            print("Pilha cheia")
            return False

        self.stack[self.topo] = v
        self.topo += 1 

    
    def pop(self):
        if self.topo < 0:
            print('Pilha vazia')
            return False

        retorno = self.stack[self.topo - 1]
        self.topo -= 1
        return retorno
    
    def peek(self):
        return self.stack[ self.topo - 1 ]

def verPilha():
    pilha = Pilha(8)

    pilha.push(1)
    pilha.push(2)
    pilha.push(3)
    pilha.push(4)
    pilha.push(5)
    pilha.push(6)
    pilha.push(7)
    pilha.push(8)
    

    print( pilha.peek() )
    # dq = pilha.pop()

    # while dq is not False:
    #     if dq:
    #         print( dq )
            
    #     dq = pilha.pop()

# verFila()
verPilha()


