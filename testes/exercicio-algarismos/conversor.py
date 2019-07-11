''' Converter algarismos romanos em algarismos arábicos '''

def converter(value):
    tabela = {
        "I" : 1, # só vem antes do V e X
        "V" : 5,
        "X" : 10, # só vem antes do L e C
        "L" : 50,
        "C" : 100, # só vem antes do D e M
        "D" : 500,
        "M" : 1000
    }

    resultado = 0
    anterior = 0
    # MCMLXXXIX

    for c in value[::-1]: # inverte a lista para ler do final
        v = tabela[c]
        m = -1 if v < anterior else +1
        resultado += v * m
        anterior = v 
    
    return resultado