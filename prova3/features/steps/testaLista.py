from behave import given, when, then

from lista import ListaEncadeada

@when(u'eu crio uma lista encadeada.')
def _when_crio_uma_lista(context):
    lista_criada = ListaEncadeada()
    context.result = lista_criada.head


@then(u'a lista criada está vazia.')
def _then_a_lista_criada_esta_vazia(context):
    assert None == context.result


@given(u'uma lista encadeada recém criada.')
def _given_uma_lista_recem_criada(context):
    context.lista = ListaEncadeada()


@when(u'eu adiciono um elemento.')
def _when_adiciono_um_elemento(context):
    context.lista.append(1)


@then(u'a lista criada não está vazia.')
def _then_a_lista_nao_esta_vazia(context):
    assert None != context.lista.head  