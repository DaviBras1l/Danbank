print("Digite o número da opção desejada:")
print("DEPÓSITO(1)")
print("SAQUE(2)")
print("EXTRATO(3)")
extrato = 4000 

resultado = int(input("Digite a opção que você deseja: "))

if resultado == 1:
    deposito = float(input("Digite a quantidade que deseja depositar: "))
    extrato += deposito
    print(f"Depósito de {deposito} realizado com sucesso.")
    print(f"Seu extrato atual é: {extrato}")
elif resultado == 2:
    saque = float(input("Digite o valor que deseja sacar: "))
    if saque > extrato:
        print("Saldo insuficiente para realizar o saque.")
    else:
        extrato -= saque
        print(f"Saque de {saque} realizado com sucesso.")
        print(f"Seu extrato atual é: {extrato}")
elif resultado == 3:
    print(f"Seu extrato é: {extrato}")
else:
    print("Opção inválida. Por favor, escolha uma opção válida (1, 2 ou 3).")