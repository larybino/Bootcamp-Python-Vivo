import funcoes

LIMITE_SAQUES = 3
AGENCIA = "0001"

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
usuarios = []
contas = []

while True:
    opcao = input(funcoes.menu())

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        saldo, extrato = funcoes.depositar(saldo, valor, extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        saldo, extrato = funcoes.sacar(
        saldo=saldo,
        valor=valor,
        extrato=extrato,
        limite=limite,
        numero_saques=numero_saques,
        LIMITE_SAQUES=LIMITE_SAQUES,
        )

    elif opcao == "e":
        funcoes.extrato(saldo, extrato=extrato)

    elif opcao == "u":
        funcoes.criar_usuario(usuarios)

    elif opcao == "c":
        numero_conta = len(contas) + 1
        conta = funcoes.criar_conta(AGENCIA, numero_conta, usuarios)

        if conta:
            contas.append(conta)

    elif opcao == "l":
        funcoes.listar(contas)

    elif opcao == "q":
        print("Operações finalizadas")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")