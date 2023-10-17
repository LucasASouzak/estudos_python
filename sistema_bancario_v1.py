menu = """
_______SELECIONE UMA OPÇÃO ABAIXO_______

[1] Deposito
[2] Saque
[3] Extrato
[0] Sair
"""
saldo = 0
limite = 500
extrato = ""
quantidade_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação inválida! Valor informado não é valido.")
            
    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))
        
        execedeu_saldo = valor > saldo
        
        exedeu_limite = valor > limite
        
        exedeu_saque = quantidade_saques >= LIMITE_SAQUES
        
        if execedeu_saldo:
            print("Operação falhou! Sem saldo suficiente para operação.")
            
        elif exedeu_limite:
            print("Operação falhou! Limite de saque execedido.")
            
        elif exedeu_saque:
            print ("Operação falhou! Limite diario de saques exedido.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque : R$ {valor:.2f}\n"
            quantidade_saques += 1
            
        else:
            print("Operação Falhou! Valor informado é inválido.")
            
    elif opcao == "3":
        print("\n_____________________EXTRATO______________________")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")
        print("==================================================")
        
    elif opcao == "0":
        break
    
    else:
        print("Opção inválida! Favor selecionar uma operação.")
        
            
        