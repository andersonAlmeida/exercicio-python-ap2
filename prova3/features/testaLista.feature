Feature: Teste de elementos existentes em uma lista encadeada

Scenario: A lista criada está vazia
    When eu crio uma lista encadeada.
    Then a lista criada está vazia.

Scenario: Após inserir um elemento na lista, ela não está mais vazia.
    Given uma lista encadeada recém criada.
    When eu adiciono um elemento.
    Then a lista criada não está vazia.