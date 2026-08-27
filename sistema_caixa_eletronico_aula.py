saldo = 1500
escolha = 0

def consulta_saldo(saldo):
    print("O saldo é: ", saldo)

def realiza_saque(valor_saque):
    valor_saque = float(input("Entre com o valor de saque: "))

    if valor_saque <=0:
        print("Valor inválido!")

    elif valor_saque > saldo:
        print("Impossível de realizar a operação")
    else:
        print("Saque realizado com sucesso")
        saldo = saldo - valor_saque
        return saldo
        
def realiza_deposito():
    valor_deposito = float(input("Entre com o valor de saque: "))
    if valor_deposito > 0:
        saldo = saldo + valor_deposito
        return saldo
    else:
        print("Operação inválida. Valor de deposito incorreto.")

def sistema_caixa():
saldo = 1500
escolha = 0

while escolha != 0:
    print("\n")
    print("1 - Consultar saldo")
    print("2 - Sacar")
    print("3 - Depositar")
    print("0 - Encerrando o sistema")

    escolha = int(input("Escolha uma opção do menu: "))

    if escolha == 1:
       consulta_saldo(saldo)

    elif escolha == 2:
       saldo = realiza_saque(saldo)

    elif escolha == 3:
         saldo = realiza_deposito(saldo)

    elif escolha == 0:
        print("Encerrando o sistema")
    
    else:
        print("Opção incorreta. Tenta novamente.")

sistema_caixa()
