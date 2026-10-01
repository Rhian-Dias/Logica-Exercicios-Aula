def validacao(matricula_usuario, senha_usuario):
    return matricula_usuario == "123" and senha_usuario == "123*"

def login():
    tentativas = 3
    for tentativa in range(1,tentativas+1):
        matricula_usuario = input("Entre com a matricula: ")
        senha_usuario = input("Entre com a senha: ")

        if validacao(matricula_usuario, senha_usuario):
            print("Bem-vindo! Acesso autorizado")
            return

        faltam = tentativas - tentativa
        if tentativas > 0:
            print("Voce ainda tem: ", faltam)

    print("Acesso bloqueado")

login()
