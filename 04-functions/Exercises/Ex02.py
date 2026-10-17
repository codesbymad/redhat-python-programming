'''Write and test a function that takes a collection of strings and returns the length of the longest string in the collection.

The application should loop through the collection of strings and rely on the value returned by the function to format all of the strings to the output such that they are all right justified to the width of the longest string.'''

def PegarMaiorTamanho(listaPalavras):
    return len(max(listaPalavras, key=len))

palavras = ["Exercise018", "Exercise029", "Exercise03uf", "Exercise04ufl", "Exercise05ifçy"]
maior = PegarMaiorTamanho(palavras)

for palavra in palavras:
    print(f"{palavra:>{maior}s}")