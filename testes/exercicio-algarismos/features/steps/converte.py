from behave import given, when, then

import conversor

@given(u'o número romano "{numero_romano}"')
def _given_o_numero_I(context, numero_romano):
    context.input = numero_romano


@when(u'quero converter em um número arábico')
def _when_quero_converter_um_numero(context):
    context.result = conversor.converter(context.input)


@then(u'o resultado é {esperado:d}')
def _then_resultado(context, esperado):
    assert esperado == context.result