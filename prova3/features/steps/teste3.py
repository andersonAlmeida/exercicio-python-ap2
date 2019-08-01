from behave import given, when, then
from lista import ListaEncadeada

@given('uma lista com os elementos [{numeros}]')
def _given_lista_com_numeros(context, numeros):
    context.lista = ListaEncadeada()
    nums = [int(n) for n in numeros.split(',')]
    for n in nums:
        context.lista.append(n)

@when('insiro o numero {num:d} no inicio')
def _when_insiro_numero(context, num):
    context.lista.prepend(num)

@then('o primeiro elemento é {expected:d}')
def _then_primeiro_elemento(context, expected):
    observed = context.lista.head.value
    assert observed == expected