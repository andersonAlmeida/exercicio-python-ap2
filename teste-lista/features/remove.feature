Feature: Implementa a remoção em uma lista 0,1,2,3,4,5,6,7,8,9
Scenario: remoção no início da lista
    Given solicitado remover o primeiro elemento
    When remove no início da lista
    Then o resultado é 1,2,3,4,5,6,7,8,9

Scenario: remoção no meio da lista
    Given o número 5 
    When removo o valor solicitado da lista 
    Then o resultado é 0,1,2,3,4,6,7,8,9

Scenario: remoção no final da lista
    Given solicitado remover o último elemento
    When removo no final da lista
    Then o resultado é 0,1,2,3,4,5,6,7,8