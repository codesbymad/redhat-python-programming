palavra = ""
palavras = dict()
while palavra != "end":
    palavra = input("Digite uma palavra ou end para finalizar o programa")
    if palavra == "end":
        break
    if palavra in palavras:
        palavras[palavra] = palavras[palavra] + 1
    else:
        palavras[palavra] = 1
for plv in sorted(palavras):
    print(f"{plv}: {palavras[plv]}")