'''Write and test a function that takes a number and a dictionary and adds the number to all values in the dictionary.

You can assume that all the values in the dictionary are numbers.'''

def AdicionarATodosOsElementos(operacao, dicionario):
    for chave, valor in dicionario.items():
        dicionario[chave] = valor + operacao

MeusNumeros = {
    "baixo": 9,
    "medio": 54,
    "alto": 99
}

AdicionarATodosOsElementos(9, MeusNumeros)
print(MeusNumeros)