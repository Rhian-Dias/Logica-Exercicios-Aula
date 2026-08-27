notas = [1.0, 3.3, 5.7, 7.8, 8.4]

def calcular_media(notas):
    for i in range(len(notas)):
        print(notas[i])

    somatorio_valores = sum(notas)
    media = somatorio_valores / len(notas)

    return somatorio_valores, media


somatorio, media = calcular_media(notas)

print("O somatório é: ", somatorio)
print("A Média é: ", media)
