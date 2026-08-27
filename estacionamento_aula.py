
def calcula_horas(horas):
    if horas <= 1:
        return 8
    elif horas >=3:
        return 15
    else:
        return 20

def cobranca_estacionamento():
    quantidade = 0
    total = 0
    veiculos_acima_3h = 0
    
    horas = float(input("Digite a quantidade de horas a se pagar: "))
        
    while horas != 0:
        preco = calcula_horas(horas)
        quantidade = quantidade + 1
        total = total + preco

        if horas > 3:
            veiculos_acima_3h = veiculos_acima_3h + 1

        horas = float(input("Digite a quantidade de horas a se pagar: "))
        

    print("A quantidade de veiculos é: ", quantidade, "O total é: ", total, "A quantidade de veiculos acima de 3h é: ", veiculos_acima_3h)

cobranca_estacionamento()
