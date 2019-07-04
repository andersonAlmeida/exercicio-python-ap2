Feature: Implementa SOMA em uma calculadora
Scenario: Soma de dois números positivos
    Given os números 2 e 4
    When calculo a soma dos números
    Then o resultado é 6

Scenario: Soma um valor com 0
    Given os números 0 e 3
    When calculo a soma dos números
    Then o resultado é 3

Scenario: Soma dois valores negativos
    Given os números -3 e -7
    When calculo a soma dos números
    Then o resultado é -10