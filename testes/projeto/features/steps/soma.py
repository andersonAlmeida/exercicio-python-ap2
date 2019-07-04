from behave import given, when, then

import calculadora

@given(u'os números {a:d} e {b:d}') # :d diz que é um decimal
def _given_dois_numeros(context, a, b):
    context.a = a
    context.b = b

@when(u'calculo a soma dos números')
def _when_executa_soma(context):
    context.resultado = calculadora.soma(context.a, context.b)

@then(u'o resultado é {expected:d}')
def _then_resultado(context, expected):
    assert expected  == context.resultado
