def main():
    # Declaração explícita de variáveis (anotações de tipo)
    i: int = 0
    n: int = 0
    soma: int = 0

    # Declaração/entrada de n
    try:
        n = int(input("Escreva o valor de n: "))
    except (ValueError, EOFError):
        print("Entrada inválida. Informe um inteiro.")
        return

    # Inicializa soma
    soma = 0

    # Para i de 1 até n faça
    for i in range(1, n + 1):
        soma = soma + i

    # Saída de dados
    print("O somatorio será:", soma)

if __name__ == "__main__":
    main()
