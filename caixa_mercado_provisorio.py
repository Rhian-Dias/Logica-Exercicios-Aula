#Codigo aula com erro para corrigir
#lembrar de colocar as funções
#lembrar de adicionar e/ou separar as variaveis globais e locais

qtd_produtos = 0
valor_total_compra = 0

def media_precos(valor_total, qtd_produtos):
    if qtd_produtos > 0:
        return valor_total/qtd_produtos
def funcao_principal():
    qtd_produtos = 0 
    valor_total_compra = 0
   
preco = float(input("Entre com o preco do produto "))

while preco != 0:
    qtd_produtos = qtd_produtos + 1
    valor_total_compra = valor_total_compra + preco

    preco = float(input("Entrte com o preco do produto"))
    media_total = media_precos(valor_total_compra, qtd_produtos)
     


     
    print(f"Quantidade produtos {qtd_produtos} ")
    print(f"Valor total da compra {valor_total_compra} ")
    print(f"valor médio {media_total} ")
    




