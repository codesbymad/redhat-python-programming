from sys import argv, exit
import os
import time

if len(argv) != 3:
    print("Usage: " + argv[0] + " <diretorio> <limiteTamanho>")
    exit(1)

diretorio = argv[1]

try:
    limiteTamanho = int(argv[2])
    arquivos = os.listdir(diretorio)
except (ValueError, OSError) as err:
    print("ERROR: " + str(err))
    exit(1)

for arquivoCheck in arquivos:
    caminhoArquivo = os.path.join(diretorio, arquivoCheck)
    if os.path.isfile(caminhoArquivo):
        dadosArquivo = os.stat(caminhoArquivo)
        if dadosArquivo.st_size > limiteTamanho:
            print(f"{arquivoCheck} {dadosArquivo.st_size} {time.ctime(dadosArquivo.st_mtime)}")