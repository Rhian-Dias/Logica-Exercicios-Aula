lista = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(lista)
for i in range(1,n):
    insert_indice = i
    valor_atual = lista.pop(i)
    for j in range(i-1, -1, -1):
        if lista[j] > valor_atual:
            insert_indice = j
    lista.insert(insert_indice, valor_atual)

print("A lista ordenada é:", lista)