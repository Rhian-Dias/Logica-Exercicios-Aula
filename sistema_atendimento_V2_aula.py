escolha = 4
normal = 0
prioridade = 0

def gerar_senha(tipo, numero):
    return f"{tipo}{numero:03d}"

def sistema_senhas():
    while escolha != 3:
        print("1 - Atendimento normal")
        print("2 - Atendimento prioritário")
        print("3 - Encerrar atendimento")
        
        escolha = int(input("Entre com uma opção: "))

        if escolha == 1:
            normal = normal + 1
            senha = gerar_senha("N", normal)
            print("A senha gerada é: ", senha)

        elif escolha == 2:
            prioridade = prioridade + 1
            senha = gerar_senha("P", prioridade)
            print("A senha gerada é: ", senha)
        
        elif escolha == 3:
            print("Encerrando o sistema.")
        
        else:
            print("Opção inválida. Digite uma opção válida.")

sistema_senhas()
