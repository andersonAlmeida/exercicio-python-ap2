Feature: Faz a iteração em uma lista encadeada de forma reversa

Scenario: Começar pelo tail da lista
Given uma lista [10,20,30,40,50]
When acesso o tail
Then o valor do primeiro elemento é 50 

Scenario: O último elemento percorrido é o head
Given uma lista [35,26,72,99,100]
When chegou ao final
Then o valor do último elemento é 35

