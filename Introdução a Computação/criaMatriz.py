from random import randint

def cria_matriz(ord):
    mat=[]
    for i in range(ordem):
        mat.append([])   #append = acrescentar, linhas
        for j in range(ordem):
            mat[i].append(randint(1,100))  # acrescenta colunas
    
    return mat

def mostra_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):   #para uma matriz não quadrada, teria que ser a qtde de elementos de uma lista, aí len(matriz[0])
            print(matriz[i][j])
        print()
        

#def transposta(mat):

#Programa Principal
ordem = int(input('Digite a ordem da sua matriz: '))
matriz = cria_matriz(ordem)
mostra_matriz(matriz)
#matriz_transposta = transposta(matriz)
#mostra_matriz(matriz_transposta)