
n = int(input("Digite a quantidade de alunos: "))
aprovados = 0
maior_media = 0
soma_notas_turma = 0

for i in range (n):
    nota1 = float(input("Digite o valor da primeira nota: "))
    nota2 = float(input("Digite o valor da segunda nota: "))

    media = (nota1 + nota2) / 2

    if media >= 6:
        situacao = "aprovado"
        aprovados = aprovados + 1
    elif media < 6:
        situacao = "reprovado"

    if maior_media < media:
        maior_media = media
    else:
        menor_media = media

    soma_notas_turma = soma_notas_turma + media
    media_turma = soma_notas_turma / n

print(f"A media das notas da turma foi de: {media_turma:.2f}")
print("A quantidade de alunos aprovados foi de: ", aprovados)
print(f"A maior média obtida foi de: {maior_media:.2f}")
