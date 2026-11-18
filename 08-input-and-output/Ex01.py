from sys import argv

for nomeArquivo in argv[1:]:
    with open(nomeArquivo, "r") as arquivo:
        linhas = palavras = caracteres = 0
        for linha in arquivo:
            linhas += 1
            caracteres += len(linha)
            palavras += len(linha.split())
    print(f"Linhas: {linhas}, palavras: {palavras}, caracteres: {caracteres}")