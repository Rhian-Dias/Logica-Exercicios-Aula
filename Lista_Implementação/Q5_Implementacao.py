quantidade = 15
positivos = 0
negativos = 0
zeros = 0
pares = 0
impares = 0
soma = 0

numeros = []

for i in range(quantidade):
    numero = int(input("Digite um valor: "))

    numeros.append(numero)
    soma = soma + numero

    if numero > 0:
        positivos = positivos + 1
    elif numero < 0:
        negativos = negativos + 1
    else:
        zeros = zeros + 1

    if numero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1

    if i == 0:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

media = soma / quantidade
acima_media = 0

for numero in numeros:
    if numero > media:
        acima_media = acima_media + 1

print("RESULTADO DOS NUMEROS")
print("A quantidade de números positivos foi de: ", positivos)
print("A quantidade de números negativos foi de: ", negativos)
print("A quantidade de zeros foi de: ", zeros)
print("A quantidade de números pares foi de: ", pares)
print("A quantidade de números ímpares foi de: ", impares)
print("O maior número foi: ", maior)
print("O menor número foi: ", menor)
print(f"A média dos números foi de: {media:.2f}")
print("A quantidade de números acima da média foram de: ", acima_media)
