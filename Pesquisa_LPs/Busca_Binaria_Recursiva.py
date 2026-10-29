def busca_binaria_recursiva(lista, inicio, fim, alvo):
    if inicio > fim:
        return -1
    
    meio = inicio + (fim - inicio) // 2
    
    if lista[meio] == alvo:
        return meio
    
    elif lista[meio] > alvo:
        return busca_binaria_recursiva(lista, inicio, meio - 1, alvo)
    
    else:
        return busca_binaria_recursiva(lista, meio + 1, fim, alvo)


numeros = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
alvo = 23

resultado = busca_binaria_recursiva(numeros, 0, len(numeros) - 1, alvo)
print(f"Elemento encontrado no índice: {resultado}") 
