'''There is a built-in function in Python called sum that will return the sum of all of the numbers of an iterable object.

Write a similar function, but instead of taking a collection as a parameter, the function should take a variable number of arguments and return the sum of them.'''

def PegarSoma(*parametros):
    return sum(parametros)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"A soma entre {numeros} é {PegarSoma(1, 2, 3, 4, 5, 6, 7, 8, 9)}")