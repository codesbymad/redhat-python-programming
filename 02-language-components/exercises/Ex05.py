'''Ask the user to input multiple numbers on one input line.
Split the numbers into a list.
Write a loop that examines each element of the list and displays the ones that are greater than zero.'''

numeros = input("Digite vários numeros separados por espaço ")

for n in numeros.split():
    if not n.isnumeric():
        continue
    if int(n) > 0:
        print(n)