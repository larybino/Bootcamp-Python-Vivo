import funcoes

usuarios = []
contas = []

while True:
    opcao = input(funcoes.menu())

    if opcao == "d":
        funcoes.depositar(usuarios)

    elif opcao == "s":
        funcoes.sacar(usuarios)

    elif opcao == "e":
        funcoes.exibir_extrato(usuarios)

    elif opcao == "u":
        funcoes.criar_cliente(usuarios)

    elif opcao == "c":
        numero_conta = len(contas) + 1
        funcoes.criar_conta(numero_conta, usuarios, contas)

    elif opcao == "l":
        funcoes.listar_contas(contas)

    elif opcao == "q":
        break

    else:
        print("\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")

