'''Write and test a function that is designed to validate input.

The function should prompt the user for a positive integer.

It should validate the information entered by the user is indeed a positive integer.

If number entered is valid, the function should return the number.

If the number entered is invalid, the function should return a zero (0) instead.

The application, not the function, should indicate with a message in the output each time an invalid entry is given.'''

def IntPos(n):
    if n >= 0:
        return n
    else:
        return 0

num = int(input("Digite um número inteiro positivo: "))
result = IntPos(num)
if result == 0:
    print(f"{num} não é um número positivo")
else:
    print(f"{num} é um numero positivo")