from sys import argv

argv.pop(0)
do_totals = False
if argv and argv[0] == "-t":
    do_totals = True
    argv.pop(0)
gLinhas = gPalavras = gCaracteres = 0

for nomeArquivo in argv:
    with open(nomeArquivo, "r") as arquivo:
        linhas = palavras = caracteres = 0
        for linha in arquivo:
            linhas += 1
            caracteres += len(linha)
            palavras += len(linha.split())
    gLinhas += linhas
    gPalavras += palavras
    gCaracteres += caracteres
    if not do_totals:
        print(f"Linhas: {linhas}, palavras: {palavras}, caracteres: {caracteres}")
if do_totals:
    print(f"Linhas: {gLinhas}, palavras: {gPalavras}, caracteres: {gCaracteres}")