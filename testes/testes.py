''' ==============================================================
Garante que o software funcione para aquilo que foi testado.

BDD - Behavior Driven Development (criar um teste do ponto de vista do usuário)

Cenário: garante uma visão estável e conhecida do sistema

- Dado um estado do sistema ->visão estável e conhecida do sistema
- Quando quero executar uma operação -> O que eu quero testar?
- Avalio o resultado -> Observado é igual ao esperado?




TDD - Test Driven Development
- Implementa o teste
- Implementa código suficiente para passar no teste
- Refatora o código
- Executa os testes novamente

***se um método retorna 0, indica que a memória está funcionando

================================================================== '''
# Gherkin

# Feature: implementar SOMA em uma calculadora.
# Scenario: Soma de dois números positivos
# Given os números 2 e 4
# When calculo a soma dos números
# Then o resultado é 6