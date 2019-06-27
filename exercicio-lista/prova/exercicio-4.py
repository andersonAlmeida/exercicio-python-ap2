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