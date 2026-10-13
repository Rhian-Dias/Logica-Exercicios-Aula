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

def selectionSort(produtos, precos):
    if not produtos:
        return produtos, precos

    for i in range(len(produtos)):
        max_i = i

        for j in range(i + 1, len(produtos)):
            if produtos[j] > produtos[max_i]:
                max_i = j

        produtos[i], produtos[max_i] = produtos[max_i], produtos[i]
        precos[i], precos[max_i] = precos[max_i], precos[i]

    return produtos, precos

def main ():
    produtos = []
    precos = []
    n = int(input("Digite a quantidade de items da lista: "))
    
    for i in range(n):
        produto = input("Entre com o nome do produto: ")
        preco = float(input("Entre com o preço do produto: "))

        produtos.append(produto)
        precos.append(preco)
    
    produtos,precos = selectionSort(produtos, precos)

    lista = []

    for i in range(n):
        lista.append([produtos[i], precos[i]])

    print("Lista como fica depois de ordenada: ")

    for item in lista:
            print("Produto:", item[0], "| Preço:", item[1])

    chave = float(input("Digite o preço do produto a ser procurado na lista: "))    

    resultado = buscaBinaria (precos, chave)

    if resultado != -1:
        print(f"O preço {chave} do produto está na lista, cujo índice é: {resultado}")
        print("Item: ", precos[resultado])
    else:
        print(f"O preço {chave} do produto não está na lista")


main()