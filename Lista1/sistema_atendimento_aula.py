normal = 0
prioridade = 0
escolha = 4

while escolha != 3:
    print("1 - Atendimento Normal")
    print("2 - Atendimento Prioritário")
    print("3 - Encerrar Atendimento")

    escolha = int(input("Entre com uma opção: "))

    if escolha == 1:
        normal = normal+1
        senha = f"N{normal:03d}"

        print("Senha gerada é: ", senha)

    elif escolha == 2: 
        prioridade = prioridade + 1
        senha = f"P{prioridade:03d}"

        print("Senha gerada é: ", senha)

    elif escolha == 3:
        print("Sistema Encerrado")

    else: 
        print("Opção inválida! ")

