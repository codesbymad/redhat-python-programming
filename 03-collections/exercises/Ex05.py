numeros = {
    0: "zero",
    1: "um",
    2: "dois",
    3: "três",
    4: "quatro",
    5: "cinco",
    6: "seis",
    7: "sete",
    8: "oito",
    9: "nove"
}

numero = input("Digite um número ")
for num in numero:
    print(numeros[int(num)], end=" ")
print()