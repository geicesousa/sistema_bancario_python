# criar funções para cada opção


# 3. extrato ambos args, args pos sado, ars nom extrato

# 4. criar usuário: usauários armazenados em uma lista, possui: nome, data_de_nascimento, CPF, endereco: {logradouro, nro, bairro, cidade/est}
# cada cpf deve ser cadatrado uma única vez e apenas números

# 5. criar conta: nº da agencia 0001


def opcoes():
    menu = '''
    ========= OPCOES =========

        [1] Depositar
        [2] Sacar
        [3] Extrato
        [0] Sair

    ==========================  
    Opcao selecionada => '''

    return input(menu)

#função deposito

def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Valor depositado: R${saldo:.2f}.\n'
        print('Depósito realizado com sucesso')
      
    else: 
        print('Houve uma falha no sistema, tente novamente mais tarde.')
    
    return valor, extrato
    
# função saque

def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > limite:
        print(f'O saque máximo é {limite}')
            
    elif numero_saques >= limite_saques:
        print(f'Você já excedeu o limite de saques mensal.')  

    elif valor < limite and valor <= saldo and valor > 0 :
        saldo -= valor
        extrato += f'Saque efetuado: R${valor:.2f}.\n'
        numero_saques += 1

        print(f'Seu saque no valor de R${valor:.2f}, foi realizado com sucesso.\n')

    else:
        print(f'Valor solicitado indisponível, seu saldo é R${saldo:.2f}.\n')
    
    return saldo, extrato

# 3. extrato ambos args, args pos sado, ars nom extrato

def exibe_extrato(saldo, /, *, extrato):
    print('\n *** EXTRATO ***')
    print(extrato)
    print(f'''Seu saldo é R${saldo:.2f}.
    ''')
    if qtd_saques > 0:
        print(f'Você ainda pode fazer {qtd_saques} saques esse mês.')
    

def main(saldo = 0
SAQUE_MAXIMO = 500
qtd_saques = 0
LIMITE_SAQUES = 3
extrato = ''
deposito = 0

while True:
    opcao = opcoes()

    if opcao == '1':
        valor_depositado = float(input('Informe a quantia que deseja depositar: \n'))
        
        saldo, extrato = deposito(saldo, valor_depositado, extrato)
      
    elif opcao == '2':
        valor_sacado = float(input('Qual a quantia que deseja sacar? '))

        saque(
            saldo=saldo, 
            valor=valor_sacado, 
            extrato=extrato, 
            limite=SAQUE_MAXIMO, numero_saques=qtd_saques, limite_saques=LIMITE_SAQUES 
        )       
    
    elif opcao == '3':
        extrato = exibe_extrato(saldo, extrato=exibe_extrato)

    elif opcao == '0':
        print('Até mais ver!')
        break
    
    else: 
        print('Digite uma opção válida')