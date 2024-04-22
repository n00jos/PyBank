## Sistema Bancario
import time

menu = '''
__________________________________
|################################|
|########### Py  Bank ###########|
|################################|
|================================|
| Qual operação deseja realizar? |
|================================|
|###    [ 1 ] - Depositar     ###|
|###    [ 2 ] - Sacar         ###|
|###    [ 3 ] - Extrato       ###|
|###    [ 4 ] - Sair          ###|
|================================|
|################################|
==================================

'''

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opc = int(input(menu))

    if opc == 1:
        valor = float(input('Depositar, qual valor deseja depositar? R$'))
        if valor > 0:   
            saldo += valor
            extrato.append([f"Deposito de R${valor:.2f}"])
            print(f'Seu saldo atual é de: R${saldo:.2f}')
            time.sleep(3)

        else:
            print('Valor não permitido, Tente novamente!')
            time.sleep(3)

    elif opc == 2:
        valor = float(input('Sacar, qual valor deseja sacar? R$'))

        if  valor > saldo:
            print(f'Saldo insuficiente. Seu saldo atual é de: R${saldo:.2f}')
            time.sleep(3)

        elif valor > limite:
            print(f'Valor acima do limite de saque permitido por saque. Seu limite atual é de R${limite:.2f}.')
            time.sleep(3)

        elif numero_saques >= LIMITE_SAQUES:
            print(f'Limite de saques diários atingido. Você só pode sacar {LIMITE_SAQUES} vezes por dia.')
            time.sleep(3)

        elif valor > 0:
            saldo -= valor
            extrato.append([f"Saque de R${valor:.2f}"])
            numero_saques += 1
            print(f'Saque realizado com sucesso. Seu saldo atual é de: R${saldo:.2f}')
            time.sleep(3)

        else:
            print('Valor não permitido, Tente novamente')
            time.sleep(3)


    elif  opc == 3:
        print('========= Extrato =========')
        for item in extrato:
             print(item)
        print('---------------------------')
        print(f'Saldo atual de R${saldo}')
        print('===========================')    
        time.sleep(5)

    elif opc == 4:
        print('Obrigado por usar o Py Bank 24hrs. Volte sempre!')
        break

    else:
        print('Operação invalida, tente novamente.')
        time.sleep(2)