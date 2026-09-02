total = 0
maior_consumo = 0
menor_consumo = 0
maior_mes = 0

for mes in range (1,13):
    consumo_mensal = float(input(f"Digite o consumo do mes: {mes}"))

    total = total + consumo_mensal

    if mes == 1:
        maior_consumo = consumo_mensal
        menor_consumo = consumo_mensal
        maior_mes = mes

    else:
        if consumo_mensal > maior_consumo:
            maior_consumo = consumo_mensal
            maior_mes = mes
        if consumo_mensal < menor_consumo:
            menor_consumo = consumo_mensal
    
media = total / 12

print("Relatorio de consumo")
print(f"O consumo total é: {total}")
print(f"O consumo médio é de: {media}")
print(f"O maior consumo atingido foi de: {maior_consumo}")
print(f"O menor consumo atingido foi de: {menor_consumo}")
