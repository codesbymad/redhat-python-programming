import json

with open("11-json/Exercises/books.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

print("Livros:")
print(dados.keys())

while True:
    livro = input("Escolha o título de um livro (ou escreva 'q' para encerrar): ")

    if livro == 'q':
        break

    info = dados.get(livro)

    if info:
        print(f"Livro: {livro}")
        print(f"""
    - autor: {info.get("author")}
    - país: {info.get("country")}
    - idioma: {info.get("language")}
    - páginas: {info.get("pages")}
    - ano: {info.get("year")}
        """)
    else:
        print("Livro não encontrado, tente novamente")