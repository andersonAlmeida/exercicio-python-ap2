from behave import given, when, then

from lista import ListaEncadeada
from iteradorLista import fromTail

@given(u'uma lista [{numeros}]')
def _given_uma_lista(context, numeros):
    context.lista = ListaEncadeada()
    nums = [int(n) for n in numeros.split(',')]
    for n in nums:
        context.lista.append(n)
        

@when(u'acesso o tail')
def _when_acesso_o_tail(context):
    context.tail = context.lista.tail


@then(u'o valor do primeiro elemento é {expected:d}')
def _then_o_valor_do_primeiro_elemento_e(context, expected):
    observed = context.tail.value
    assert observed == expected


@when(u'chegou ao final')
def _when_chegou_ao_final(context):
    context.ultimo = fromTail(context.lista)


@then(u'o valor do último elemento é {numero:d}')
def _then_o_valor_do_ultimo_elemento(context, numero):
    observed = context.ultimo.value
    assert observed == numero