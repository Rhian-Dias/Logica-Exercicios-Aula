def busca_binaria(lista, chave):
    esq = 0
    dir = len(lista) - 1

    while esq <= dir:
        meio = (esq + dir) // 2

        if lista[meio] == chave:
            return meio
        
        elif chave < lista[meio]:
            dir = meio - 1
        else:
            esq = meio + 1

    return -1

numeros = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
chave = 23

resultado = busca_binaria(numeros, chave)

if resultado != -1:
    print(f"Elemento encontrado no índice {resultado}.")
else:
    print("Elemento não encontrado na lista.")
