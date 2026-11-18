import os

arquivo = open(os.path.join(os.path.dirname(__file__), "dataset"), "r")
linhas = arquivo.readlines()
arquivo.close()

compOwners = {}

for linha in linhas:
    owner, compType, value = linha.split()
    value = int(value)
    equipamento = compOwners.get(owner)

    if not equipamento:
        equipamento = {}

    if compType in equipamento:
        equipamento[compType] += value
    else:
        equipamento[compType] = value

    compOwners[owner] = equipamento

print(compOwners)