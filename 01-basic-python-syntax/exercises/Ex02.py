''' Write a program that prompts twice for text from the user.
The first input should be a first name.
The second input should be a last name.
The program should print the full name on one line and the person's initials on the second line. '''

nome = input("Digite o seu primeiro nome ")
sobrenome = input("Digite o seu sobrenome ")
print(nome, sobrenome, sep=" ")
print(nome[0], sobrenome[0], sep="")