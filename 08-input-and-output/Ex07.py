from sys import argv, exit

if len(argv) != 3:
    print("Usage: " + argv[0] + " <arquivo1> <arquivo2>")
    exit(1)

arquivo1 = open(argv[1], "r")
arquivo2 = open(argv[2], "r")

set1 = set()
for linha in arquivo1:
    set1.add(linha.strip())

set2 = set()
for linha in arquivo2:
    set2.add(linha.strip())

arquivo1.close()
arquivo2.close()

set3 = set1 & set2

for linha in set3:
    print(f" - {linha}")
