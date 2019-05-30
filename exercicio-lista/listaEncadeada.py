# classe nó
# classe lista encadeada 

class No:
    def __init__(self, v):
        self.value = v
        self.next = None


class ListaEncadeada:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def prepend(self, v):
        #cria nó de v
        no = No(v)

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

        #o tail é o novo nó
        self.tail = no


    def tail(self):
        if self.head is None:
            return None
        
        iter = self.head

        while iter.next is not None:
            iter = iter.next

        return iter
    
    # def append(self, v):
    #     final = self.tail()

    #     #cria nó de v
    #     no = No(v)

    #     if final is None:
    #         final = no
    #         self.head = final
    #     else:
    #         #final aponta p/ o novo nó
    #         final.next = no

    # def tail(self):
    #     if self.head is None:
    #         return None
        
    #     iter = self.head

    #     while iter.next is not None:
    #         iter = iter.next

    #     return iter

    def printLista(self):
        if self.head is None:
            print("Lista vazia")
        
        iter = self.head

        print(iter.value)

        while iter.next is not None:
            print(iter.next.value)
            iter = iter.next

    def remove(self, v):
        if self.head is None:
            return None
        
        iter = self.head

        if iter.value == v:
            if iter.next is None:
                print("Lista destruida")
                return True
            self.head = iter.next
            return True

        prevNo = None

        while iter.next is not None:

            if iter.value == v:
                if prevNo is not None:
                    prevNo.next = iter.next
                    return True
                else:
                    self.head = iter.next
                    return True
            
            prevNo = iter
            iter = iter.next 



lista = ListaEncadeada()

lista.append(1)
lista.append(2)
lista.append(3)
lista.append(4)
lista.prepend(5)
lista.prepend(6)
lista.append(7)

# lista.remove(2)


lista.printLista()
