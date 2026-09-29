# Escreva um programa que solicite ao usuário que insira uma frase. O programa deve determinar e imprimir as seguintes informações: o primeiro caractere da frase e quantas vezes ele ocorre na frase; o último caractere da frase e quantas vezes ele ocorre na frase.

frase = input("Insira uma frase ")
priCarac = frase[0]
tamanho = len(frase)
ultCarac = frase[tamanho-1]
print(f"essa é a primeira caractere: {priCarac}")
print(f"A caractere {priCarac} aparece {frase.find(priCarac)}")
print(f"Essa é a última caractere da frase: {ultCarac}")
print(f"A caractere {ultCarac} aparece {frase.find(ultCarac)}")