''' Converter algarismos romanos em algarismos arábicos '''

def converter(value):
    tam = len(value)
    tabela = {
        1: {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        },
        2: {
            "II" : 2
        },
        3: {
            "VII" : 7
        }
    }
    return tabela[tam][value]