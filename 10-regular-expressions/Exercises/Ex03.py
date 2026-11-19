import re

while True:
    produto = input("Digite um produto (ou digite 'fim' para sair): ").strip()

    if produto == "fim":
        break

    regex = r"^(\d{2})([A-Z]{2})[ \t]+(.+)$"
    encontrar = re.search(regex, produto)

    if encontrar:
        print(f"Digitos: {encontrar.group(1)}")
        print(f"Letras: {encontrar.group(2)}")
        print(f"Descrição: {encontrar.group(3)}")
    else:
        print("Essa não é a descrição válida para um produto")