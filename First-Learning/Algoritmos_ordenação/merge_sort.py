def mergeSort(lista):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    metade_esquerda = lista[:meio]
    metade_direita = lista[meio:]

    esquerda_ordenada = mergeSort(metade_esquerda)
    direita_ordenada = mergeSort(metade_direita)

    return merge(esquerda_ordenada, direita_ordenada)

def merge(esquerda, direita):
    resultado = []
    i = j = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])

    return resultado

lista_nao_ordenada = [3, 7, 6, -10, 15, 23.5, 55, -13]
lista_ordenada = mergeSort(lista_nao_ordenada)
print("A lista ordenada é: ", lista_ordenada)