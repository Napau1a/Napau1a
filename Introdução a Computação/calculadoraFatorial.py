'''
Lógica do exercício:

função:
- função para calcular o fatorial de um número:
- retorna o cálculo do fatorial para quem chamou

programa principal:
- leitura de um valor inteiro
- chamar para fatorial
- mostrar fatorial calculado

'''
'''

def calculo_fatorial(x):
    fat=1
    for i in range (1,x+1):
        fat= fat*i
    return fat
    

print("Vamos calcular o fatorial de um número inteiro!")
n = (int(input("Digite aqui o valor desejado: ")))
print(f'O resultado é: {calculo_fatorial(n)}')

'''


''' Fazer o cálculo de uma combinação
C = número de combinações
n = número total de objetos no conjunto
r = número de opções de objetos do conjunto
'''

def calculo_fatorial(x):
    fatorial=1
    for i in range(1,x+1):
       fatorial= fatorial*i
    return fatorial

def combinação(a,b):
    return calculo_fatorial(a)/(calculo_fatorial(a-b)*calculo_fatorial(b))

print("Vamos fazer o cálculo de uma combinação!")
m = int(input('Digite aqui o valor que de m: '))
p = int(input('Digite aqui o valor que de p: '))
print(f'O valor da combinação é = {combinação(m,p)}')