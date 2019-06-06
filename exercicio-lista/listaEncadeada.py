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


    def printLista(self):
        if self.head is None:
            print("Lista vazia")
            return False
        
        iter = self.head
        prev = None        

        while iter.next is not None:
            if prev is None:
                print('head: ' + str(iter.value))
            else:
                print(iter.value)

            iter = iter.next
            prev = iter
        
        if iter.next is None:
            print('tail: ' + str(iter.value))


    def remove(self, v):
        if self.head is None: #se não existe o head a lista não existe, caso 0 elementos
            print("Lista inexistente")
            return None
        
        iter = self.head #seta o head como início

        if iter.value == v: #se o primeiro nó é o valor desejado
            if iter.next is None: # se não tem um próximo valor, caso 1 elemento
                self.head = None 
                print("Lista destruida")
                return True

            self.head = iter.next #seta como início o próximo nó, caso N elementos remove o primeiro elemento
            return True

        prevNo = None #seta o ponteiro que salva o nó anterior

        while iter.next is not None: #itera pela lista, caso N elementos

            if iter.value == v: #se é o valor que quero remover                 
                if prevNo is not None: #verifica se é o head #se não é o head
                    prevNo.next = iter.next #aponta o nó anterior para o próximo nó
                    return True
            
            prevNo = iter #atualiza a referência para o nó anterior
            iter = iter.next #atualiza o iterador
        
        #verifica o último nó
        if iter.value == v:
            if iter.next is None: #se for o último nó
                prevNo.next = None #remove o ponteiro do nó anterior
                self.tail = prevNo # seta o nó anterior como tail
                return True
        
        print('Valor não encontrado na lista.')



lista = ListaEncadeada()

lista.append(3)
lista.append(4)
lista.append(5)
lista.append(6)
lista.prepend(2)
lista.prepend(1)
lista.append(7)

lista.printLista()


lista.remove(7)


lista.printLista()
