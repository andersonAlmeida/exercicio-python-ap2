class Fila2:
    def __init__(self, size=100):
        self.data = [None] * size
        self.head = 0
        self.tail = 0

    def enqueue(self, value):
         if self.tail < len(self.data):
            self.data[self.tail] = value
            self.tail += 1
         else:
            raise Exception("Fila cheia")

    # def dequeue(self, value):
    #      if self.tail == self.head:
    #         raise Exception("Fila vazia.")
    #      value = self.head
    #      self.head += 1
    #      return value
    
    def dequeue(self):
        if self.tail == self.head:
            raise Exception("Fila vazia.")

        value = self.head
        self.head += 1
        return value

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

'''
    1 - Qual o(s) problema(s) que essa implementação pode apresentar?

    O método dequeue recebe um valor, que não deveria ser necessário porque a remoção em uma fila deveria ser sempre o elemento no início da fila. Outro problema é que ela não é otimizada para utilizar os espaços que vão sendo liberados no início da fila, ela não implementa um buffer circular.

'''

fila = Fila(5)

fila.enqueue(4)
fila.enqueue(1)
fila.enqueue(2)
fila.enqueue(3)
# fila.enqueue(5)

print( fila.dequeue() )

fila.enqueue(5)


print( fila.dequeue() )
print( fila.dequeue() )
print( fila.dequeue() )
print( fila.dequeue() )
# print( fila.dequeue() )
























'''
    3 - Por que a inserção no ínicio de uma lista na linguagem de programação Python é tão mais lenta que a inserção no final dessa mesma lista?

    Porque todos os demais elementos tem que ser deslocados para uma próxima posição, enquanto a inserção no final da lista não precisa.

'''

'''
    4 - Dada uma lista encadeada com as operações prepend(value), que insere um elemento no início da lista; append(value), que insere um elemento no final da lista; removeFirst() -> value, que remove e retorna o elemento no início da lista; removeLast() -> value, que remove e retorna o elemento no final da lista, implemente uma classe Pilha, que possui o comportamento de uma estrutura LIFO (Last In, First Out), e que possua os métodos push(value), para inserção, pop() -> value, para exclusão, e peek() -> value, para consultar, sem remover, o próximo elemento.
'''

class No:
    def __init__(self, v):
        self.value = v
        self.next = None
        self.before = None
    
    def insertBefore(self, v):
        no = No(v)
        no.before = self.before
        self.before.next = no
        no.next = self        
        self.before = no
    
    def insertAfter(self, v):
        no = No(v)
        no.next = self.next
        self.next.before = no
        no.before = self
        self.next = no

class ListaEncadeada:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def prepend(self, v):
        #cria nó de v
        no = No(v)

        #se existe um head
        if self.head is not None:
            #aponta o head para o novo no que o antecede
            self.head.before = no

        #v.next aponta p/ head
        no.next = self.head

        #head aponta p/ o novo nó
        self.head = no

        #procura o último elemento para setar o tail
        iter = self.head
        while iter.next is not None:
            iter = iter.next
        self.tail = iter
        

    def append(self, v):
        final = self.tail

        #cria nó de v
        no = No(v)
        
        #final aponta p/ o novo nó
        if final is None:
            final = no
            self.head = final
        else:
            final.next = no
            #aponta para o no anterior
            no.before = final 

        #o tail é o novo nó
        self.tail = no

    def removeFirst(self):
        firstElm = self.head # guarda o elemento que será removido
        self.head = self.head.next # aponta o head para o elemento seguinte
        
        if self.head is not None and self.head.next is not None:
            self.head.next.before = None # remove o apontamento para o no que está sendo removido

        return firstElm # retorna o elemento removido

    def removeLast(self):
        lastElm = self.tail # guarda o elemento que será removido
        self.tail = self.tail.before # aponta o tail para o elemento anterior
        self.tail.next = None # remove o apontamento para o no que está sendo removido

        return lastElm # retorna o elemento removido


class Pilha:
    def __init__(self, lista):
        self.stack = lista
        self.topo = None
        

    def push(self, v):
        self.stack.prepend(v)
        self.topo = self.stack.head 

    
    def pop(self):
        if self.topo is None:
            print('Pilha vazia')
            return False

        retorno = self.stack.removeFirst()
        self.topo = self.stack.head
        return retorno
    
    def peek(self):
        if self.topo is not None:
            return self.topo
        else:
            print("Pilha vazia")
            return False


def mostraPilha():
    lista = ListaEncadeada()
    
    pilha = Pilha(lista)

    pilha.push(1)
    pilha.push(2)
    pilha.push(3)
    pilha.push(4)
    pilha.push(5)

    # dq = pilha.pop()

    # while dq is not False:
    #     if dq:
    #         print( dq.value )
            
    #     dq = pilha.pop()
    
    # if pilha.peek() is not False:
    #     print("topo da pilha: ", pilha.peek().value )


# mostraPilha()


def fromHead():
    lista = ListaEncadeada()

    lista.prepend(2)
    lista.append(3)
    lista.append(4)
    lista.append(5)
    lista.append(6)
    lista.prepend(1)
    lista.append(7)

    # print(lista.removeFirst().value)
    # print(lista.removeLast().value)

    iter = lista.head    

    while iter.next is not None:

        if iter.value == 5:
            iter.insertAfter(88)
        
        print(iter.value)

        iter = iter.next
    
    if iter.next is None:
        print(iter.value)

# fromHead()
