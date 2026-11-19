import re

while True:
    anum = input("Digite um número inteiro (ou digite 'fim' para sair): ").strip()

    if anum == "fim":
        break

    check = re.search(r"^-?\d+$", anum)

    if not check:
        print("Esse não é um número válido")
        continue

    if anum[0] == '-':
        print("Esse número é negativo")
    elif anum == "0":
        print("Esse número é zero")
    else:
        print("Esse número é positivo")