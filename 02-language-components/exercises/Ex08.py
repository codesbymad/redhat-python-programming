'''Rewrite exercise # 4 such that the program takes into account the case where the first number entered is bigger than the last.
For example, if the user inputs the numbers 10 and 15, then the sum would be 75.
10 + 11 + 12 + 13 + 14 + 15 = 75
If the user inputs the numbers 15 and 10, then the sum would be still be 75.'''

'''Write a program that prompts twice for an integer.
The program should output the sum of the integers within the range of those two numbers inclusively.'''

num1 = int(input("Digite um número "))
num2 = int(input("Digite outro número "))
cont = 0
soma = 0
if num1 < num2:
    cont = num1
    while cont != num2+1:
        soma = soma + cont
        cont = cont + 1
elif num2 < num1:
    cont = num2
    while cont != num1+1:
            soma = soma + cont
            cont = cont + 1
else:
    soma = num1
print(f"A soma dos numeros durante o intervalo de {num1} até {num2} é {soma}")