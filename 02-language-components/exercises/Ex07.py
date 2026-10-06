'''Use a range to loop through and print each number from 0 to 49 to produce the following output.
Each number should be printed individually as opposed to concatenating them as a string.'''

cont = 0
while cont != 50:
    if cont < 10:
        print(" ", end="")
    print(cont, end=" ")
    if cont % 10 == 9:
        print()
    cont = cont + 1