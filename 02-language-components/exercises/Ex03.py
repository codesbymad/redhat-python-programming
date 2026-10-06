'''Write a program that prompts twice for an integer.
The program should print the larger of the two numbers.
If the numbers are equal, then the program should indicate it as such.'''

num1 = float(input("Digite um número "))
num2 = float(input("Digite outro número "))
if num1 > num2:
    print(f"O número {num1} é maior que o número {num2}")
elif num2 > num1:
    print(f"O número {num2} é maior que o número {num1}")
else:
    print(f"O número {num1} é igual ao número {num2}")