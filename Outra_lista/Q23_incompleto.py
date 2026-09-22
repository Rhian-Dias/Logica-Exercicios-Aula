tentativas = 3
senha_correta = "Tech2026"

senha = input("Digite uma senha: ")

while tentativas >= 3:
    if senha != senha_correta:
        print("Senha digitada incorreta. Digite novamente.")
        tentativas = tentativas - 1
        print("Tentativas restantes: ", tentativas)
        senha = input("Digite uma senha: ")

    elif tentativas < 0:
        print("Acesso bloqueado. Limite máximo atingido.")

    else: 
        senha == senha_correta
        print("A senha foi digitada corretamente")

