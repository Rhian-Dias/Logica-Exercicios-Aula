def soma(a,b):
    return a+b
    #resultado1 = soma(a,b)
    #print("A soma é: ", resultado1)

def subtracao(a,b):
    return a-b
    #resultado2 = subtracao(a,b)
    #print("A subtração é: ", resultado2)

def multiplicacao(a,b):
    return a*b
    #resultado3 = multiplicacao(a,b)
    #print("A multiplicação é: ", resultado3)

def divisao(a,b):
    return a/b
    #resultado4 = divisao(a,b)
    #print("A divisão é: ", resultado4)


#a = float(input("Digite o valor do primeiro número: "))
#b = float(input("Digite o valor do segundo número: "))
opcao_menu = 0

while opcao_menu != 5:
    print("Entre com uma das opções disponíveis:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

    opcao_menu = int(input("Informe a opção: "))

    if opcao_menu == 5:
            print("Encerrando o sistema...")
            print("Obrigado por utilizar o sistema!")
            break

    if opcao_menu >= 1 and opcao_menu <= 4:
        a = float(input("Digite o valor do primeiro número: "))
        b = float(input("Digite o valor do segundo número: "))

        if opcao_menu == 1:
            print("Operação de Soma escolhida")
            resultado1 = soma(a,b)
            print("A soma é: ", resultado1)

        elif opcao_menu == 2:
            print("Operação de Subtração escolhida")
            resultado2 = subtracao(a,b)
            print("A soma é: ", resultado2)

        elif opcao_menu == 3:
            print("Operação de Multiplicação escolhida")
            resultado3 = multiplicacao(a,b)
            print("A soma é: ", resultado3)

        elif opcao_menu == 4:
            print("Operação de Divisão escolhida")
            resultado4 = divisao(a,b)
            print("A soma é: ", resultado4)   
     
    else:
        print("Erro: Opção inválida")
        print("Digite uma opção entre os números de 1 a 5.")
