print(" == Menu Bancario ==")

saldo = 0.0
limite = 500.0
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input("\n[d] Depositar \n[s] Sacar \n[e] Extrato \n[q] Sair \n=> ").lower()

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: R$ "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Erro! O valor do depósito deve ser maior que zero.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: R$ "))

        if valor <= 0:
            print("Erro! O valor informado é inválido.")
        elif valor > saldo:
            print("Erro! Você não tem saldo suficiente.")
        elif valor > limite:
            print("Erro! O valor do saque excede o limite de R$ 500,00 por operação.")
        elif numero_saques >= LIMITE_SAQUES:
            print("Erro! Você já atingiu o limite de 3 saques diários.")
        else:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso!")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        if extrato == "":
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("=========================================")

    elif opcao == "q":
        print("Sistema encerrado. Obrigado por utilizar nosso banco!")
        break
    else:
        print("Opção inválida! Por favor, selecione uma opção do menu.")