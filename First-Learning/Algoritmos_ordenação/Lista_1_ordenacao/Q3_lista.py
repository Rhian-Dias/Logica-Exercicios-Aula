def buscaBinaria(lista, chave):
    pos_ini = 0
    pos_fim = len(lista) - 1

    while pos_ini <= pos_fim:
        pos_meio = (pos_ini + pos_fim) // 2

        if lista[pos_meio] == chave:
            return pos_meio
        if lista[pos_meio] < chave:
            pos_fim = pos_meio - 1
        else:
            pos_ini = pos_meio + 1

    return -1

def selectionSort(notas, nomes):
    if not notas:
        return notas, nomes

    for i in range(len(notas)):
        max_i = i

        for j in range(i + 1, len(notas)):
            if notas[j] > notas[max_i]:
                max_i = j

        notas[i], notas[max_i] = notas[max_i], notas[i]
        nomes[i], nomes[max_i] = nomes[max_i], nomes[i]

    return notas, nomes

def main():
    nomes = []
    notas = []

    n = int(input("Digite a quantidade de alunos: "))

    for i in range(n):
        nome = input("Digite o nome do aluno: ")
        nota = float(input("Digite a nota do aluno: "))

        nomes.append(nome)
        notas.append(nota)

    notas, nomes = selectionSort(notas, nomes)

    lista = []

    for i in range(n):
        lista.append([nomes[i], notas[i]])

    print("Alunos ordenados da maior para a menor nota:")

    for aluno in lista:
        print("Nome:", aluno[0], "| Nota:", aluno[1])

    chave = float(input("\nDigite a nota que deseja buscar: "))

    resultado = buscaBinaria(notas, chave)

    if resultado != -1:
        print(f"A nota {chave} está na lista, no índice {resultado}.")
        print("Aluno:", nomes[resultado])
    else:
        print(f"A nota {chave} não está na lista.")

main()