def fatorial (n):
    resultado = 1

    for i in range (1, n+1):
        resultado *= i

    return resultado


n = int(input("Digite o valor de n: "))

print(fatorial(n))

#limite no n = 1559
