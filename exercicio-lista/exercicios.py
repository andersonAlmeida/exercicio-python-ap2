'''
1) Criar uma função em Python que receba uma lista e retorne a soma dos elementos.

2) Criar uma função em Python que receba duas listas e retorne o produto escalar das duas listas.

3) Dada uma lista, encontre todos os elementos de valor par cercados por elementos de valor ímpar.

4) Dado o seguinte código Python:

a = [1, 2, 3, 4, 5, 6]

b = a

b [1] = 1

Qual o valor de a[1]? Por quê? 2 porque a na posição 1 é igual a 2, a contagem começa do 0

5) Uma lista, em Python, pode armazenar qualquer tipo de dado, logo, podemos armazenar listas dentro de listas. Implemente um classe Matriz, que permite a criação de matrizes. Deve ser possíveil acessar e alterar qualquer elemento da matriz. Crie métodos para a soma, subtração e multiplicação de duas matrizes,
'''

minhaLista = [2,5,10,1,2,3,8,10]
minhaLista2 = [10,10,10,10,10,10,10,10]

#1
def somaLista( lista ):
    resultado = 0
    for valor in lista:
        resultado += valor
    
    return resultado #pode retornar sum(lista)

# print( somaLista( minhaLista ) )

#2
def produtoEscalar( lista1, lista2 ):
    prod = []
    i = 0
    
    for val in lista1:
        prod.append( val * lista2[i] )
        i += 1

    return sum( prod )

#melhor forma
def prodEscalar(a, b):
    soma = 0
    
    for i in range( len(a) ):
        soma += a[i] * b[i]

    return soma

# print( produtoEscalar( minhaLista, minhaLista2 ) )

#3 Dada uma lista, encontre todos os elementos de valor par cercados por elementos de valor ímpar.
def encontraNumParEntreImpars( lista ):
    resultado = []
    i = 0
    
    if len(lista) > 2:
        for val in lista:
            if i > 0 and i <= (len(lista) - 2) and val % 2 == 0:
                if lista[i-1] % 2 != 0:
                    if lista[i+1] % 2 != 0:
                        resultado.append( val )
            i += 1
    
    return resultado

# print( encontraNumParEntreImpars( minhaLista ) )

#4 a[1] é igual a 1, porque b é uma referência de a

'''
5) Uma lista, em Python, pode armazenar qualquer tipo de dado, logo, podemos armazenar listas dentro de listas. Implemente um classe Matriz, que permite a criação de matrizes. Deve ser possíveil acessar e alterar qualquer elemento da matriz. Crie métodos para a soma, subtração e multiplicação de duas matrizes
'''
class Matriz:
    def __init__(self, linhas = 1, colunas = 1):
        self.matriz = [ [0 for x in range(linhas)] for y in range(colunas) ]

    @property 
    def get_matrix(self):
        return self.matriz
        


mtx = Matriz(3,3)

for x in range( len(mtx.matriz) ):
    for y in range( len(mtx.matriz[x]) ):
        print( 'posicao x y : ' + str(x) + ' ' + str(y) + ' valor:' + str(mtx.matriz[x][y]) )