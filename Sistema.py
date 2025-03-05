#   CRIAÇÃO DAS VARIAVEIS
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
extrato = ""
limite = 500
numero_de_saques = 0
LIMITE_DE_SAQUES = 3

#   LOOP DO SISTEMA
while True :
    opcao = input(menu)
    
    if opcao == "d":

        valor = float(input("Informe o valor do deposito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R${valor:.2f}\n"
        else:
            print("A operacao falhou! Valor invalido para deposito.")

    elif opcao == "s":

        saque = float(input("Informe o valor do saque: "))
        
        excedeu_saques = numero_de_saques >= LIMITE_DE_SAQUES
        excedeu_saldo = saque > saldo
        excedeu_limite = saque > limite

        if excedeu_saques:
            print("A operação falhou! Limite de saques atingido.")
        elif excedeu_saldo:
            print("A operação falhou! Saldo insuficiente.")
        elif excedeu_limite:
            print("A operação falhou! O valor do saque é maior que o limite.")
        else:
            saldo -= saque
            numero_de_saques += 1
            extrato += f"Saque: R${saque:.2f}\n"

    elif opcao == "e":
        print("=============EXTRATO==============")
        print("Não foram realizadas movimentacoes." if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print("==================================")
    
    elif opcao == "q":
        break
    
    else:
        print("Operação invalida, por favor selecione a operação desejada.")
        

        
