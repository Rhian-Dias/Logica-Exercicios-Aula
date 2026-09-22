qntd_excelentes = 0
soma_percentuais = 0

n = int(input("Digite a quantidade de funcionários a serem cadastrados: "))

for i in range (n):
    nome = input("Digite o nome do funcionario: ")
    qntd_tarefas_realizadas = int(input("Digite a quantidade de tarefas totais do funcionário: "))
    qntd_no_prazo = int(input("Digite a quantidade de tarefas realizadas pelo funcionário dentro do prazo estipulado: "))
    qntd_faltas = int(input("Digite a quantidade de faltas que o funcionário teve durante o prazo estipulado: "))

    percentual = (qntd_no_prazo / qntd_tarefas_realizadas) * 100

    if percentual >= 90 and qntd_faltas <= 2:
        classificacao = "excelente"
        qntd_excelentes = qntd_excelentes + 1

    elif percentual >= 75 and qntd_faltas <= 4:
        classificacao = "bom"

    elif percentual >= 60:
        classificacao = "regular"

    elif percentual < 60:
        classificacao = "necessita acompanhamento"

    else:
        classificacao = "impossível determinar"

    if i == 0:
        maior_percentual = percentual
        menor_percentual = percentual
    elif maior_percentual > percentual:
        maior_percentual = percentual
    elif menor_percentual < percentual:
        menor_percentual = percentual

    soma_percentuais = soma_percentuais + percentual
    media_percentuais = soma_percentuais / n


print("RELATORIO DOS FUNCIONARIOS CADASTRADOS")
print("O nome do funcionario é: ", nome)
print("O percentual do funcionário é de: ", percentual)
print("A classificação do funcionário é: ", classificacao)
print("A média percentual dos funcionários foi de: ", media_percentuais)
print("A quantidade de funcionários em padrão de excelência é de: ", qntd_excelentes)
