'''Write a program that prompts the user for a string and then prompts again for a number.
The program should create and print a new string by using the repetition operator on the string and the number.
For example, if the string is hello and the number is 3, then hellohellohello should be printed.'''

string = input("Digite uma palavra ")
num = int(input("Digite um número "))
print(string*num)