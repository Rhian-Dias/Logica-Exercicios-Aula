lista = [1,2,3,4]
chave = 4

def buscaSequencial(lista, chave):
    n = len(lista)
    for indice in range (n):
        if lista[indice] == chave:
            return indice
    return -1

print(buscaSequencial(lista,chave))

