def main():
    soma = 0
    while True:
        try:
            num = input("Digite um número: ")
            soma += int(num)
        except ValueError:
            print("Número inválido")
        except KeyboardInterrupt:
            print("\nPrograma interrompido pelo usuário.")
            break
        except EOFError:
            break

    print(f"A soma de todos os números digitados é {soma}")
if __name__ == "__main__":
    main()
