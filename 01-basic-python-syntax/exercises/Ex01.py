''' Write a program that prompts to enter a string of text.
The program should print the original text followed on a second line in the output by the number of characters entered. '''

string = input("Digite um texto ")
print(f"Você escreveu {string}")
print(f"Seu texto contém {len(string)} caracteres")