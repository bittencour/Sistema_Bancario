menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor que deseja deposinar: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor: .2f}\n"
        else:
            print("Falha na operação! O valor informado é invalido")
    elif opcao == "s":
        valor = float(input("Informe qual o valor que gostaria de sacar: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Não é possivel realizar esta operação, pois seu saldo é insuficiente.")
        elif excedeu_limite:
            print("Não é possivel realizar esta operação, pois o valor excede o limite.")
        elif excedeu_saques:
            print("Não é possivel realizar esta operação, número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {-valor: .2f}\n"
        else:
            print("Falha na operação! O valor informado é invalido")

    elif opcao == "e":
        print("\n========== EXTRATO ==========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo: .2f}")
        print("===============================")
    elif opcao == "q":
        break

    else:
        print("Operação inválida, selecione novamente a operação que deseja realizar.")