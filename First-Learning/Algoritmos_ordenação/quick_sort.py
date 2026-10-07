def particao(lista, baixo, alto):
    pivot = lista[alto]
    i = baixo - 1

    for j in range(baixo, alto):
        if lista[j] <= pivot:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]

    lista[i+1], lista[alto] = lista[alto], lista[i+1]
    return i+1

def quicksort(lista, baixo=0, alto=None):
    if alto is None:
        alto = len(lista) - 1

    if baixo < alto:
        pivot_indice = particao(lista, baixo, alto)
        quicksort(lista, baixo, pivot_indice-1)
        quicksort(lista, pivot_indice+1, alto)

lista = [64, 34, 25, 12, 22, 11, 90, 5]
quicksort(lista)
print("A lista ordenada é:", lista)