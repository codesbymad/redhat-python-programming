import json
import re

frequencias = {}
maisFrequente = ""
maiorContagem = 0

with open("11-json/Exercises/cyclone", "r", encoding="utf-8") as cyclone:
    for linha in cyclone:
        for palavra in linha.split():
            encontrar = re.search(r"\w+", palavra)

            if not encontrar:
                continue

            palavra = encontrar.group(0).lower()

            if frequencias.get(palavra):
                frequencias[palavra] += 1
            else:
                frequencias[palavra] = 1

            if frequencias[palavra] > maiorContagem:
                maisFrequente = palavra
                maiorContagem = frequencias[palavra]

with open("11-json/Exercises/frequencias.json", "w", encoding="utf-8") as frequencia:
    json.dump(frequencias, frequencia, indent="\t", ensure_ascii=False)

if maisFrequente:
    print(f"'{maisFrequente}' ocorreu {maiorContagem} vezes")
else:
    print("O arquivo não possui palavras para contar.")