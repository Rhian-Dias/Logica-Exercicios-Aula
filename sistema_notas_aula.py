def media(qntd_notas):
    total = 0
    for i in range(qntd_notas):
        notas = float(input("Entre com as notas: "))
        total = total + notas

return total / qntd_notas


def situacao_aluno(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"


def sistema_notas():
    qntd_notas = int(input("Digite a quantidade de notas para trabalhar: "))
    total_notas = float(input("Entre com os valores de notas: "))
    
    #for i in range(qntd_notas):
        
    media_total = media(qntd_notas)
    status = situacao_aluno(media_total)
    print(status, media_total)


sistema_notas()
