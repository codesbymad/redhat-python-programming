# Write and test a function that takes two lists as parameters and returns a list of the elements that are common to both.

def PegarElementosEmComum(lista1, lista2):
    s1 = set(lista1)
    s2 = set(lista2)
    return list(s1 & s2)

l1 = ["Teste", 689, "ta terminando"]
l2 = [689, "acaba", 89, "Teste"]

print(PegarElementosEmComum(l1, l2))