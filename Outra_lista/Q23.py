tentativas = 3
senha_correta = "Tech2026"
tentativas_usadas = 0
acesso_valido = False

senha = input("Digite uma senha: ")

while tentativas > 0 and acesso_valido == False:
    tentativas_usadas = tentativas_usadas + 1

    if senha == senha_correta:
        acesso_valido = True
        print("A senha foi digitada corretamente. Acesso concedido.")
        print("Quantidade de tentativas utilizadas: ", tentativas_usadas)

    else:
        tentativas = tentativas - 1
        if tentativas > 0:
            print("Senha digitada incorreta. Digite novamente.")
            print("Tentativas restantes: ", tentativas)
            senha = input("Digite uma senha: ")
        else:
            print("Acesso bloqueado. Limite máximo atingido.")
