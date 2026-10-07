lista = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(lista)
for i in range(n):
    min_indice = i
    for j in range(i+1, n):
        if lista[j] < lista[min_indice]:
            min_indice = j   
    lista[i], lista[min_indice] = lista[min_indice], lista[i]

print("A lista ordenada é: ", lista)