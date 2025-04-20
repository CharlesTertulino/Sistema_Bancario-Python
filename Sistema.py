#   CRIAÇÃO DAS VARIAVEIS
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

valor_saldo = 0
valor_extrato = ""
limite = 500
numero_de_saques = 0
LIMITE_DE_SAQUES = 3

banco_de_usuarios = {}
banco_de_contas = {}

#   FUNCOES DO SISTEMA

def Criar_Usuario(cpf, nome, endereco, data_nasc):
    if cpf not in banco_de_usuarios :
        banco_de_usuarios[f"{cpf}"] = {
            "nome" : nome, 
            "endereco" : endereco, 
            "data_nasc" : data_nasc
            }
        print(f"Usuario {nome} criado com sucesso!")
    else :
        print(f"O Usuario {nome} ja existe.")

def Criar_Conta(num_conta, usuario):
    banco_de_contas[f"{num_conta}"] = {
        "usuario" : usuario,
        
    }

def saque(valor):
    #   VARIAVEIS DE CONDICAO
    excedeu_saques = numero_de_saques >= LIMITE_DE_SAQUES
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite

    #   VERIFICA SE O SAQUE ESTA INDISPONIVEL
    if excedeu_saques:
        print("A operação falhou! Limite de saques atingido.")
    elif excedeu_saldo:
        print("A operação falhou! Saldo insuficiente.")
    elif excedeu_limite:
        print("A operação falhou! O valor do saque é maior que o limite.")
    else:
        #   EXECUTA O SAQUE MANIPULANDO AS VARIAVEIS
        saldo -= valor
        numero_de_saques += 1
        extrato += f"Saque: R${valor:.2f}\n"

    return saldo

def depositar(valor, saldo, extrato):
    #   VERIFICA A VALIDADE E REALIZA O DEPOSITO
    if valor > 0:
        saldo += valor
        extrato += f"Deposito: R${valor:.2f}\n"
    else:
        print("A operacao falhou! Valor invalido para deposito.")
    return saldo

def emitir_extrato(saldo, extr):
    print("=============EXTRATO==============")
    print("Não foram realizadas movimentacoes.") if not extr else extr
    print(f"\nSaldo: R${saldo:.2f}")
    print("==================================")

#   LOOP DO SISTEMA
while True :
    opcao = input(menu)
    
    match(opcao):
        case "d":
            #valor_deposito = float(input("Informe o valor do deposito: "))
            #depositar(valor = valor_deposito, saldo = saldo)
            print("depositou")
        case "s":
            #valor_saque = float(input("Informe o valor do saque: "))
            #saque(valor = valor_saque)
            print("sacou")
        case "e":
            #emitir_extrato(saldo = saldo, extr = extrato)
            print("extrato")
        case "q":
            print("quitou")
            break
        case _:
            print("Operação invalida, por favor selecione a operação desejada.")

    