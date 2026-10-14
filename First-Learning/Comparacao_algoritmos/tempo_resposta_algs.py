import time

def fatorialIterativo (n):
    resultado = 1

    for i in range (1, n+1):
        resultado *= i

    return resultado


def fatorialRecursivo (n):
    if n==0 or n==1:
        return 1
    return n*fatorialRecursivo(n-1)


n = int(input("Digite um valor para n: "))


a = fatorialIterativo(n)
inicio_a = time.perf_counter()
fim_a = time.perf_counter()
tempo_decorrido_a = fim_a - inicio_a

b = fatorialRecursivo(n)
inicio_b = time.perf_counter()
fim_b = time.perf_counter()
tempo_decorrido_b = fim_b - inicio_b


print(f"Tempo de resposta de fatorial iterativo é: {tempo_decorrido_a:.10f}")
print(f"Tempo de resposta de fatorial recursivo é: {tempo_decorrido_b:.10f}")

