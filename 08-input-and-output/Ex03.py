arquivoEntrada = input("Em qual arquivo você deseja ler? ")
arquivoSaida = input("Em qual arquivo você deseja escrever? ")

openEntrada = open(arquivoEntrada, "r")
openSaida = open(arquivoSaida, "w")

while True:
    linha = openEntrada.readline()
    if not linha:
        break
    openSaida.write(linha)

openEntrada.close()
openSaida.close()