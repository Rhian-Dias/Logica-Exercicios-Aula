def emprestar_livros(livros_disponiveis, livros_emprestados):
    if livros_disponiveis > 0:
        livros_disponiveis = livros_disponiveis - 1
        livros_emprestados = livros_emprestados + 1
        print("Livros emprestados com sucesso")
    else:
        print("Falta de livros disponíveis na biblioteca para empréstimo")
    return livros_emprestados,livros_disponiveis

def devolver_livros(livros_disponiveis, livros_emprestados):
    if livros_emprestados > 0:
        livros_emprestados = livros_emprestados - 1
        livros_disponiveis = livros_disponiveis + 1
        print("Livros devolvidos com sucesso")
    else:
        print("Não há livros emprestados a serem devolvidos")
    return livros_emprestados,livros_disponiveis

def consultar_livros(livros_disponiveis, livros_emprestados):
    print(f"Livros disponíveis na Biblioteca: {livros_disponiveis}")
    print(f"Livros emprestados na Biblioteca: {livros_emprestados}")

def encerrar_sistema():
    print("Encerrando sistema.")

def main():
    livros_disponiveis = 50
    livros_emprestados = 0

    escolha = 10

    while escolha != 0:
        print("Sistema de Biblioteca")
        print("1 - Emprestar Livros")
        print("2 - Devolver Livros")
        print("3 - Consultar estoque de Livros")
        print("0 - Sair do Sistema")

        escolha = int(input("Digite o numero da opção desejada: "))
        
        if escolha == 1:
            emprestar_livros(livros_disponiveis, livros_emprestados)

        elif escolha == 2:
            devolver_livros(livros_disponiveis, livros_emprestados)

        elif escolha == 3:
            consultar_livros(livros_disponiveis, livros_emprestados)

        elif escolha == 0:
            encerrar_sistema()

        else:
            print("Escolha incorreta inserida pelo usuário. Tente novamente.")
    

main()
