Feature: Teste de inserção em uma lista

Scenario: Inserção de número positivo no início da lista
Given uma lista com os elementos [1,2,3,4,5]
When insiro o numero 37 no inicio
Then o primeiro elemento é 37

Scenario: Inserção de número negativo no início da lista 
Given uma lista com os elementos [1,2,3,4,5]
When insiro o numero -10 no inicio
Then o primeiro elemento é -10