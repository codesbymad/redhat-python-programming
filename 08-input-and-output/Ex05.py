from sys import argv, exit

if len(argv) != 3:
    arquivoEntrada = input("Em qual arquivo você deseja ler? ")
    arquivoSaida = input("Em qual arquivo você deseja escrever? ")
else:
    arquivoEntrada = argv[1]
    arquivoSaida = argv[2]

try:
    openEntrada = open(arquivoEntrada, "r")
    openSaida = open(arquivoSaida, "w")
except OSError as err:
    print("ERROR: " + str(err))
    exit(1)

for linha in openEntrada:
    openSaida.write(linha)

openEntrada.close()
openSaida.close()