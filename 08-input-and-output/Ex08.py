from sys import argv

argv.pop(0)

names = {}

for curr_file in argv:
    fileproc = open(curr_file, "r")
    for line in fileproc:
        line = line.strip()
        if line in names.keys():
            names[line] += 1
        else:
            names[line] = 1
    fileproc.close()

for name, freq in names.items():
    print(f"{name}: {freq}")