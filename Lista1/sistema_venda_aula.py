def calcular_valor_vendas(quantidade, preco):
    return quantidade * preco

def calcular_meta(valor_total):
    if valor_total >= 5000:
        return "Meta diária alcançada"
    else:
        falta = 5000 - valor_total
        return f"Meta diária não alcançada. Faltam: , {falta:.2f}"

def main():
        
    quantidade = 0
    valor_total = 0
    maior_venda = 0

    cod_produto = int(input("Entre com o codigo do produto: "))

    while cod_produto != 0:
        quantidade = int(input("Entre com a quantidade: "))
        preco = float(input("Entre com o preço: "))

        valor_vendas = calcular_valor_vendas(quantidade, preco)    

        quantidade_vendas = quantidade_vendas + 1
        valor_total = valor_total + valor_vendas

        if valor_vendas > maior_venda:
            maior_venda = valor_vendas

        cod_produto = int(input("Entre com o codigo do produto: "))

    print("RELATORIO DE VENDAS")
    print("Quantidade de vendas realizadas: ", quantidade_vendas)
    print("O valor total das vendas realizadas foi de: ", valor_total)
    print("O valor de maior venda realizada foi de: ", maior_venda)

    meta = calcular_meta(valor_total)
    print(meta)


main()
