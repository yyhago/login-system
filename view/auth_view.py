from controller.auth_controller import ControllerUser

while True:
    print("======= SISTEMA DE LOGIN =======")
    print("""
        1 - Cadastrar Conta
        2 - Realizar Login
    """)
    print("================================")

    try:
        opcao_usuario = int(input("Seja bem-vindo ao sistema!\nO que deseja fazer (1 - Cadastro | 2 - Login)? "))
    except ValueError:
        print("Por favor, insira apenas números válidos.\n")
        continue

    if opcao_usuario == 1:
        email = input("Insira seu melhor email: ")
        password = input("Insira uma senha segura: ")
        resultado = ControllerUser.register_login(email, password)
        print(resultado.get("mensagem") or resultado.get("erro"))

    elif opcao_usuario == 2:
        email = input("Insira seu email: ")
        password = input("Insira sua senha: ")
        resultado = ControllerUser.login_account(email, password)

        if "mensagem" in resultado:
            print(resultado["mensagem"])
        else:
            print(resultado["erro"])

    else:
        print("Opção inválida. Tente novamente.")
