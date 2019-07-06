Feature: Implementa a adição em uma lista 0,1,2,3,4,5,6,7,8,9
Scenario: Adição no início da lista
    Given o número 16
    When adiciono no início da lista
    Then o resultado é 16,0,1,2,3,4,5,6,7,8,9

Scenario: Adição no meio da lista
    Given o número 35 
    When adiciono após o valor 4 elemento 
    Then o resultado é 0,1,2,3,4,35,5,6,7,8,9

Scenario: Adição no final da lista
    Given o número 50
    When adiciono no início da lista
    Then o resultado é 0,1,2,3,4,5,6,7,8,9,50