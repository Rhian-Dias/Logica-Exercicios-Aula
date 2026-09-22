numero_secreto = 27
tentativas = 0

palpite = int(input("Digite um valor como palpite: "))

while palpite != numero_secreto:
    tentativas = tentativas + 1

    if palpite < numero_secreto:
        print("Tente novamente usando um número maior.")
    else:
        print("Tente novamento usando um número menor.")

    palpite = int(input("Digite outro valor como palpite: "))

tentativas = tentativas + 1
print("Parabéns! Você acertou.")
print("Quantidade de tentativas: ", tentativas)


if tentativas <= 5:
    print("Excelente!")
elif tentativas <= 10:
    print("Bom!")
else:
    print("Precisa melhorar.")
