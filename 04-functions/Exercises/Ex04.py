'''Rewrite the function in Exercise 3 above to return a tuple instead of a sum.

The tuple should be the sum and the average of all of the arguments passed to the function.'''

def PegarSomaEMedia(*parametros):
    calc_soma = sum(parametros)
    calc_media = calc_soma/len(parametros)
    return (calc_soma, calc_media)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"A soma e a média entre {numeros} é {PegarSomaEMedia(1, 2, 3, 4, 5, 6, 7, 8, 9)}")