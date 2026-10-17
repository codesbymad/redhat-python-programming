'''Write and test a function that takes a variable number of arguments as its first parameter and a number as its second parameter.

The function should return the count of the values in the tuple parameter (the variable number of arguments) that are greater than the second parameter (num in the sample below).

For example, one such call to a function named positive is shown below.

res = positive(5, -10, 10, -20, 30, num=0)
In this case, the function would return a value of 3.'''

def Numeros(*lista, limite):
    n = 0
    for item in lista:
        if item > limite:
            n += 1
    return n

print(Numeros(5, -10, 10, -20, 30, limite=0))