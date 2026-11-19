import json
import requests

while True:
    try:
        num = input("Digite um número positivo (ou digite 'fim' para encerrar o programa): ")

        if num == 'fim':
            break

        num = int(num)

        if num <= 0:
            print("Digite um número positivo.")
            continue

    except ValueError:
        print("Esse não é um número válido, tente novamente")
        continue

    fact1Resp = requests.get(f"http://numbersapi.com/{num}/?json&notfound=floor")
    fact2Resp = requests.get(f"http://numbersapi.com/{num}/math/?json&notfound=floor")

    if fact1Resp.status_code != 200:
        fact1 = f"Nenhuma informação encontrada. Código: {fact1Resp.status_code}"
    else:
        fact1 = fact1Resp.json().get("text")

    if fact2Resp.status_code != 200:
        fact2 = f"Nenhuma informação matemática. Código: {fact2Resp.status_code}"
    else:
        fact2 = fact2Resp.json().get("text")

    print(f"Número {num}:\n{fact1}\n{fact2}")