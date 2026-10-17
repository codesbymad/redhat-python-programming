'''Write a calculator application that presents the following menu:

Calculator options:
      1. Add
      2. Subtract
      3. Multiply
      4. Divide
      5. Quit
The user is expected to enter a number from the above menu.

After choosing the operation, the user should be prompted twice for 2 numbers and the chosen operation performed on them with the result being displayed on the screen.

Each of the above options should be implemented as its own function'''

def adicao():
    x, y = PegarNumeros()
    print(f"{x} + {y} == {x + y}")

def subtracao():
    x, y = PegarNumeros()
    print(f"{x} - {y} == {x - y}")


def multiplicacao():
    x, y = PegarNumeros()
    print(f"{x} * {y} == {x * y}")

def divisao():
    x, y = PegarNumeros()
    print(f"{x} / {y} == {x / y}")

def PegarNumeros():
    x = int(input("Digite o primeiro número: "))
    y = int(input("Digite o segundo número: "))
    return x, y

def sair():
    exit()

def Invalido():
    print("operação invalida")

calculadora = {
    "1": adicao,
    "2": subtracao,
    "3": multiplicacao,
    "4": divisao,
    "5": sair
}

while True:
    print("Operacoes matematicas: ")
    for op in calculadora:
        print(f"{op}: {calculadora[op].__name__}")
    escolha = input("Escolha uma dessas operações matemáticas: ")
    calculadora.get(escolha, Invalido)()