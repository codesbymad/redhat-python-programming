'''Write a program that creates a loop asking the user to input a number.

Repeat this process until the user enters the value end.

The following can be used to loop through the user input.

prompt = "Enter a number (or the word 'end' to quit) "
while True:
    data = input(prompt)
    if data == "end":
        break
    #Remainder of while loop goes here
Add each iteration number to a list.

Just before the program ends, print the following:

The contents of the list on one line

The sum of the elements in the list on the second line'''

num = ""
list = list()
while num != "end":
    num = input("Insira um número (ou a palavra 'end' para sair)")
    if num == "end":
        break
    list = list + [int(num)]
print(list)
soma = sum(list)
print(soma)