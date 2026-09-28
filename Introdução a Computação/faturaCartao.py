'''
    Entrada de Dados:
Digite o nome do cliente: Fulano de Tal
Digite o dia de vencimento: 9
Digite o mês de vencimento: Janeiro
Digite o valor da fatura: 350,00

    Saída de Dados:
Olá, Fulano de Tal
A sua fatura com vencimento em 9 de Janeiro no valor de R$ 350,00 está fechada
'''
'''
Nome = input('Digite aqui o nome do cliente: ')
Dia = input('Digite aqui o dia de vencimento da fatura: ')
Mês = input('Digite aqui o mês de vencimento da fatura: ')
Valor = input('Digite aqui o valor total da fatura: R$')

print(f'Bem-vinde, {Nome}')
print(f'A sua fatura com vencimento em {Dia} de {Mês}, no valor de R${Valor} está fechada!')
'''
Nome = input('Digite aqui o nome do cliente: ')
Dia = input('Digite aqui o dia de vencimento da fatura: ')

if Dia<=0 :
    print('Ops! Você informou a data incorretamente, tente novamente!')


elif Dia>31 :
     print('Ops! Você informou a data incorretamente, tente novamente!')
    

else: 
    Mês = input('Digite aqui o mês de vencimento da fatura: ')

Valor = input('Digite aqui o valor total da fatura: R$')

print(f'Bem-vinde, {Nome}')
print(f'A fatura com vencimento em {Dia} de {Mês}, no valor de R${Valor} está fechada!')