''' Write a program that accepts a string from the user.
Determine and print the following information about the string:
Does it end in a period?
Does it contain all alphabetic characters?
Is there an 'x' in the string?
Create and print a new string that has all occurrences of e changed to E. '''

inp = input("Digite algo ")
print("Ela termina com um ponto final? ", inp.endswith("."))
print("Ela contém apenas caracteres alfabéticos? ", inp.isalpha())
print("Há um 'x' na string? ", "x" in inp)
print(inp.replace("e", "E"))