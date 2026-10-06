palavra = ""
palavras = set()
while palavra != "end":
    palavra = input("Digite uma palavra ou end para finalizar o programa")
    if palavra == "end":
        break
    if palavra in palavras:
        print("Essa palavra já está armazenada")
        continue
    else:
        palavras.add(palavra)
print(sorted(palavras))
print(f"A quantidade de palavras é {len(palavras)}")