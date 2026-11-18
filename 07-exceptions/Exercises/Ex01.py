def main():
    alist = [410, 497, 647, 9, 8, 86, 46, 4, 8, 684]
    while True:
        try:
            num = input("Digite um número ou 'fim' para sair?: ")
            if num == 'fim':
                break
            num = int(num)
        except ValueError:
            print("entrada inválida")
            continue

        try:
            if num < 0:
                raise IndexError("Não digite indices negativos")
            print(f"O número no indice {num} é {alist[num]}")
        except IndexError:
            print("Não há um número para esse indice")

if __name__ == "__main__":
    main()