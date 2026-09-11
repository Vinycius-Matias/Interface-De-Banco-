# FUNÇÕES FINANCEIRAS

def criar_conta():
    while True:
        try:
            saldo = float(input("Digite o saldo inicial da conta: R$ "))
            if saldo < 0:
                print("Saldo inicial não pode ser negativo.")
            else:
                print("Conta criada com sucesso!")
                return saldo
        except ValueError:
            print("Digite um valor válido.")


def depositar(saldo):
    try:
        valor = float(input("Digite o valor do depósito: R$ "))
        if valor <= 0:
            print("O depósito deve ser maior que zero.")
        else:
            saldo += valor
            print("Depósito realizado com sucesso!")
    except ValueError:
        print("Valor inválido.")

    return saldo


def sacar(saldo):
    try:
        valor = float(input("Digite o valor do saque: R$ "))
        if valor <= 0:
            print("O saque deve ser maior que zero.")
        elif valor > saldo:
            print("Saldo insuficiente.")
        else:
            saldo -= valor
            print("Saque realizado com sucesso!")
    except ValueError:
        print("Valor inválido.")

    return saldo


def consultar_saldo(saldo):
    print(f"Saldo atual: R$ {saldo:.2f}")


#MENU PRINCIPAL

def menu():
    saldo = criar_conta()

    while True:
        print("\n====== MENU ======")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Consultar saldo")
        print("4 - Encerrar programa")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            saldo = depositar(saldo)

        elif opcao == "2":
            saldo = sacar(saldo)

        elif opcao == "3":
            consultar_saldo(saldo)

        elif opcao == "4":
            print("Sistema encerrado.")
            break

        else:
            print("Opção inválida.")


#EXECUÇÃO
menu()