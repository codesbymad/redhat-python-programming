from sys import argv

if len(argv) != 3:
    arquivoEntrada = input("Em qual arquivo você deseja ler? ")
    arquivoSaida = input("Em qual arquivo você deseja escrever? ")
else:
    arquivoEntrada = argv[1]
    arquivoSaida = argv[2]

openEntrada = open(arquivoEntrada, "r")
openSaida = open(arquivoSaida, "w")

while True:
    linha = openEntrada.readline()
    if not linha:
        break
    openSaida.write(linha)

openEntrada.close()
openSaida.close()