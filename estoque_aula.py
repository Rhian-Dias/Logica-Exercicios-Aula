estoque = 100
escolha = 4

while escolha != 0:
    print("\n")
    print("1 - Entrada de unidades")
    print("2 - Saida de unidades")
    print("3 - consulta de unidades do estoque")
    print("0 - Fechar programa")

    escolha = int(input("Escolha uma opção do menu: "))

    if escolha == 1:
        quantidade = int(input("Insira a quantidade de unidades de entrada: "))
        estoque = estoque + quantidade

        print("Deu certo! Estoque atualizado...")

    elif escolha == 2:
        quantidade = int(input("Digite a quantidade a ser retirada do estoque: "))

        if quantidade <= estoque:
            estoque = estoque - quantidade
            print("Saída realizada com sucesso! ")
        else: 
            print("Estoque insuficiente!")

    elif escolha == 3:
        print(" O estoque atualizado é: ", estoque)

    elif escolha == 0:
        print("Sistema finalizado!")

    else:
        print("Escolha de opção inálida. Tente novamente!")