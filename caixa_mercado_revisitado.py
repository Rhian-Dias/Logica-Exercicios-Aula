#erros de funcionamento corrigidos
qtd_produtos = 0
valor_total = 0

def media_precos(valor_total, qtd_produtos):
    if qtd_produtos > 0:
        return valor_total / qtd_produtos

def funcao_principal(valor_total, qtd_produtos):
    preco = float(input("Entre com o preco do produto "))

    while preco != 0:
        qtd_produtos = qtd_produtos + 1
        valor_total = valor_total + preco
        preco = float(input("Entre com o preco do produto "))

    media_total = media_precos(valor_total, qtd_produtos)
        
    print(f"Quantidade produtos {qtd_produtos} ")
    print(f"Valor total da compra {valor_total} ")
    print(f"valor médio {media_total} ")

print(funcao_principal(valor_total, qtd_produtos))
