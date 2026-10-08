def buscaBinaria(lista, chave):
    pos_ini = 0
    pos_fim = len(lista) - 1

    while pos_ini <= pos_fim:
        pos_meio = (pos_ini + pos_fim) // 2

        if lista[pos_meio] == chave:
            return pos_meio
        if lista[pos_meio] > chave:
            pos_fim = pos_meio - 1
        else: 
            pos_ini = pos_meio + 1

    return -1

def merge(esquerda,direita,comparar):
	resultado = [] 
	i,j = 0,0
	while (i < len(esquerda) and j < len(direita)):
		if comparar(esquerda[i],direita[j]):
			resultado.append(esquerda[i])
			i += 1
		else:
			resultado.append(direita[j])
			j += 1
	while (i < len(esquerda)):
		resultado.append(esquerda[i])
		i += 1
	while (j < len(direita)):
		resultado.append(direita[j])
		j += 1
	return resultado

def mergeSort(lista, comparar = lambda x, y: x < y):
	if len(lista) < 2:
		return lista[:]
	else:
		middle = len(lista) // 2
		esquerda = mergeSort(lista[:middle], comparar)
		direita = mergeSort(lista[middle:], comparar)
		return merge(esquerda, direita, comparar) 


def main ():
    lista = []
    n = int(input("Digite a quantidade de elementos da lista: "))
    
    for i in range(n):
        elemento = int(input("Entre com os valores da lista: "))

        lista.append(elemento)
    
    lista = mergeSort(lista)

    chave = int(input("Digite o valor a ser procurado na lista: "))    

    print(f"Lista como fica depois de ordenada: {mergeSort(lista)}")

    resultado = buscaBinaria (lista, chave)
    
    if resultado != -1:
        print(f"O elemento {chave} está na lista, cujo índice é: {resultado}")
    else:
        print(f"O elemento {chave} não está na lista")

main()

