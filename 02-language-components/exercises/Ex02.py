# Rewrite the preceding exercise to additionally print out how many digits are in the number, if the number is an integer.

lucky_num = input("Digite algo ")
if not lucky_num.isnumeric():
    print(f"O número {lucky_num} não é um número")
else:
    print(f"O número {lucky_num} é um número e possui {len(lucky_num)} dígitos")