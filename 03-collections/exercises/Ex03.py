'''Write a program that creates a loop asking the user to input a number.

Repeat this process until the user enters the value end.

Enter each number into a set.

Before you enter the number, verify if the number is already in the set.

If the number is already in the set, then update a counter that tracks how many entries are not added to the set.

Just before the program ends, print the following:

The contents of the set on one line

The number of elements that were NOT added to the set on the second line'''

num = ""
numeros = set()
entrN = 0
while num != "end":
    num = input("Digite um número ou end para terminar ")
    if num == "end":
        break
    if num in numeros:
        print("Esse número ja foi armazenado")
        entrN = entrN + 1
        continue
    else:
        numeros.add(num)
print(numeros)
print(f"A quantidade de tentativas de inserir números repetidos foi {entrN}")