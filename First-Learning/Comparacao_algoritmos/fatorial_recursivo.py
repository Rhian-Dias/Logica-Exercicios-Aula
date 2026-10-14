def fatorial (n):
    if n==0 or n==1:
        return 1
    return n*fatorial(n-1)


n = int(input("Entre com o valor de n: "))
teste = fatorial(n)
print(teste)

#limite no n = 1000
