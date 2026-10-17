'''While the index method of a list can be used to find either the first occurrence of an item or the first occurrence of it within a range of the list, it does not allow you to find, say the second or third occurrence by passing in a number as to the one you are looking for.

Write a function that takes 3 parameters and returns what it finds.

One being the list to search.

The second being the object to search for.

The third being an int representing which one you are looking for such as the first, second, third occurrence.

The index method raises a ValueError exception if the value being searched for does not exit in the list.

It is perfectly fine for your function to behave in the same manner.'''

def NumeroDeOcorrencias(lista, item, num):
    if lista.count(item) < num:
        return -1

    comeca_em = 0
    for x in range(num):
        achado_em = lista.index(item, comeca_em)
        comeca_em = achado_em + 1

    return achado_em

minhaLista = ["Teste", 46, "Teste", 46, "Teste", [9, 8, 7], "Teste", "Testando"]

print(f"A terceira ocorrencia de 'Teste' está no index: {NumeroDeOcorrencias(minhaLista, 'Teste', 3)}")