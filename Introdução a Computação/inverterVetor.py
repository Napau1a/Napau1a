'''
1) - Faça uma função que recebe como parâmetro de entrada um vetor de tamanho qualquer, 
e retorna como resultado o vetor invertido. 
Exemplo: ao receber como entrada o vetor v = [3, 5, 7, 9], 
a função deve retornar o vetor x = [9,7, 5, 3].
'''

''' 
from random import randint

def inverter_vetor(vet):
    aux=[]
    for i in range(len(vet)-1,-1,-1):   #Limite superior, inferior, -1 pra indicar que é decrescente
        aux.append(vet[i])
    return aux

vetor = []

quant = int(input('Digite a quantidade de elementos do seu vetor: '))

for i in range(quant):
    vetor.append(randint(1,100))

print(vetor)
print(inverter_vetor(vetor))
'''

##Depois do feedback do prof:
from random import randint

def inverter_vetor(vet):
    aux=[]
    return aux=[::-1]

vetor = []

quant = int(input('Digite a quantidade de elementos do seu vetor: '))

for i in range(quant):
    vetor.append(randint(1,100))

print(vetor)
print(inverter_vetor(vetor))