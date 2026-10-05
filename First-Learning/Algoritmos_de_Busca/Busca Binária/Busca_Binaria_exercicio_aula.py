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


def main ():
    lista = []
    n = int(input("Digite a quantidade de elementos da lista: "))
    
    for i in range(n):
        elemento = int(input("Entre com os valores da lista: "))

        lista.append(elemento)
    
        lista.sort

    chave = int(input("Digite o valor a ser procurado na lista: "))    

    resultado = buscaBinaria (lista, chave)

    if resultado != -1:
        print(f"O elemento {chave} está na lista")
    else:
        print(f"O elemento {chave} não está na lista")

main()

