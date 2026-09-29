'''Write a program that prompts twice for an integer.
Print the product of the two numbers.
Once this works properly, try entering numbers with a decimal point.
What happens? Why?
Now try entering data that is nonnumerical.
What happens? Why?'''

n1 = int(input("Digite um número "))
n2 = int(input("Digite outro número "))
prod = n1 * n2
print(f"O produto entre {n1} e {n2} é {prod}")
