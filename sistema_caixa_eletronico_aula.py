def consulta_saldo(saldo):
    print("Seu saldo é: ", saldo)

def realiza_saque(saldo):
    valor_saque = float(input("Entre com o valor de saque: "))
    
    if valor_saque <= 0:
        print("Valor inválido!")
    elif valor_saque > saldo:
        print("Saldo insuficiente!")
    else:
        saldo = saldo - valor_saque
        print("Saque realizado com sucesso!")

        return saldo

def realiza_deposito(saldo):
    valor_deposito = float(input("Entre com o valor a ser depositado!"))
    
    if valor_deposito > 0:
        saldo = saldo + valor_deposito

        return saldo
    else:
        print("Valor de depósito incorreto")

def sistema_caixa():
    saldo = 1500 

    escolha = 1

    while escolha != 0:
        print("1 - Consultar saldo")
        print("2 - Sacar")
        print("3 - Depositar")
        print("0 - Sair")

        escolha = (input("Entre com uma opção: "))

        if escolha == 1:
            consulta_saldo(saldo)

        elif escolha == 2:
            saldo = realiza_saque(saldo)
            
        elif escolha == 3:
            saldo = realiza_deposito(saldo)
        
        elif escolha == 0:
            print("Operação finalizada!")

        else:
            print("Opção incorreta. Tente Novamente!!")

sistema_caixa()





