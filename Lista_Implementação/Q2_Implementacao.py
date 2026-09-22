soma_medias = 0
aprovados = 0
recuperacao = 0
reprovados = 0
maior_media = 0
posicao_maior = 0

n = int(input("Digite um valor para a quantidade de alunos: "))

for notas in range(n):
    print("INFORMAÇÕES NOTAS DO ALUNO")

    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    media = (nota1 + nota2) / 2
    soma_medias = soma_medias + media

    if media >= 7:
        situacao = "Aprovado"
        aprovados = aprovados + 1
    elif media >= 5:
        situacao = "Recuperação"
        recuperacao = recuperacao + 1
    else:
        situacao = "Reprovado"
        reprovados = reprovados + 1

    print(f"Média: {media:.2f}")
    print("Situação: ", situacao)

    if notas == 0:
        maior_media = media
        posicao_maior = notas + 1
    elif media > maior_media:
        maior_media = media
        posicao_maior = notas + 1

media_geral = soma_medias / n

print("RELATORIO DA TURMA")
print(f"Média geral da turma: {media_geral:.2f}")
print("Quantidade de alunos aprovados: ", aprovados)
print("Quantidade de alunos em recuperação: ", recuperacao)
print("Quantidade de alunos reprovados: ", reprovados)
print(f"Maior média obtida: {maior_media:.2f}")
print("Posição do aluno com maior média: ", posicao_maior)
