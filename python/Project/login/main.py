def inicio():
    emailCorreto = "renan.meira@gmail.com"
    senhaCorreta = "123456"

    email = input("Digite seu email: ")

    if email == emailCorreto:
        senha = input("Digite sua senha: ")

        if senha == senhaCorreta:
            print("Login bem-sucedido!")
        else:
            print("Senha incorreta.")
    else:
        print("Email incorreto.")

inicio()