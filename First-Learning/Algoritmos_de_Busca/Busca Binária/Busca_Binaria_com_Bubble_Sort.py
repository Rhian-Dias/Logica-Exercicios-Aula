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


def bubbleSort(lista):
    n = len(lista)
    for i in range(n-1):
        for j in range(n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]


def main ():
    lista = []
    n = int(input("Digite a quantidade de elementos da lista: "))
    
    for i in range(n):
        elemento = int(input("Entre com os valores da lista: "))

        lista.append(elemento)
    
    bubbleSort(lista)

    chave = int(input("Digite o valor a ser procurado na lista: "))    

    print(f"Lista como fica depois de ordenada: {lista}")

    resultado = buscaBinaria (lista, chave)
    
    if resultado != -1:
        print(f"O elemento {chave} está na lista, cujo índice é: {resultado}")
    else:
        print(f"O elemento {chave} não está na lista")

main()

