import re

while True:
    anum = input("Digite um número real (ou digite 'fim' para sair): ").strip()

    if anum == "fim":
        break

    check = re.search(r"^-?\d+\.\d+$", anum)

    if not check:
        print("Esse não é um número real válido")
        continue

    if anum[0] == '-':
        print("Esse número é negativo")
    else:
        print("Esse número é positivo")