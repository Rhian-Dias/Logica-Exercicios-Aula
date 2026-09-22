valor_sacado = int(input("Digite o valor que deseja sacar: R$ "))

if valor_sacado <= 0:
    print("Valor inválido. Impossível realizar saque. Necessário que o valor seja positivo.")
else:
    restante = valor_sacado

    notas100 = restante // 100
    restante = restante % 100

    notas50 = restante // 50
    restante = restante % 50

    notas20 = restante // 20
    restante = restante % 20

    notas10 = restante // 10
    restante = restante % 10

    if restante != 0:
        print("O saque não pode ser realizado")
    else:
        print("RELATORIO DO SAQUE")
        print("Notas de R$ 100: ", notas100)
        print("Notas de R$ 50: ", notas50)
        print("Notas de R$ 20: ", notas20)
        print("Notas de R$ 10: ", notas10)
