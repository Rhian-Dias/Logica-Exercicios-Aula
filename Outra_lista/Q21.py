
n = 8
total = 0
acima_100 = 0

for i in range (n):
    venda = int(input("Digite o valor da venda: "))

    total = total + venda

    if venda >100:
        acima_100 = acima_100 + 1
    
    if i == 0:
        maior_venda = venda
        menor_venda = venda
    if maior_venda < venda:
        maior_venda = venda
    elif menor_venda > venda:
        menor_venda = venda

media = total / n

print ("O total das vendas foi de: ", total)
print("O valor de maior venda foi de: ", maior_venda)
print("A media das vendas no dia foi de: ", media)
