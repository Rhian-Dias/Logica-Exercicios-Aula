total_vendas = 0
acima_100 = 0

for i in range(10):
    venda = float(input("Digite o valor da venda: R$ "))
    total_vendas = total_vendas + venda

    if venda > 100:
        acima_100 = acima_100 + 1
        
    if i == 0:
        maior = venda
        menor = venda
    else:
        if venda > maior:
            maior = venda
        if venda < menor:
            menor = venda

media = total_vendas / 10

print("RELATORIO VENDAS")
print(f"Total vendido: R$ {total_vendas:.2f}")
print(f"Média das vendas: R$ {media:.2f}")
print("Vendas acima de R$ 100,00: ", acima_100)
print(f"Maior venda: R$ {maior:.2f}")
print(f"Menor venda: R$ {menor:.2f}")
