def funcao01():
    print("modulo " + __name__ + ", funcao " + funcao01.__name__)

def funcao02():
    print("modulo " + __name__ + ", funcao " + funcao01.__name__)

def main():
    print("Testando módulo: ") 
    funcao01()
    funcao02

if __name__ == "__main__":
    main()