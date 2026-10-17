# Write and test a function that receives a list as its only parameter and returns a new list of the positive elements only.

def ApenasPositivos(lista):
    result = []
    for elemento in lista:
        if not (type(elemento) == int or type(elemento) == float):
            continue
        if elemento > 0:
            result.append(elemento)
    return result

elementos = ["Teste", 47869, -456, 689, 46.468, "testando", [9, 8, 7], -46]
print(f"Elementos: {elementos}")
resultado = ApenasPositivos(elementos)
print(f"Resultados: {resultado}")