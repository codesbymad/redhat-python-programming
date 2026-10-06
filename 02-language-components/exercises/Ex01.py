# Write a program that prompts for a lucky number. The program should print out a message if the number entered is not an integer.

lucky_num = input("Digite algo ")
if not lucky_num.isnumeric():
    print(f"O número {lucky_num} não é um número")