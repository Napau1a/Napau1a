from random import randint

def MAX(A):
    maior = 0

    for i in range(len(A)):
        linha = A[i]

        for j in range(len(linha)):
            valor = linha[j]
            if valor > maior:
                maior = valor
                lin = i
                col = j
    
    

    return maior, lin+1, col+1 #para que não comece em 0x0


#Programa Principal
ordem_i = 0
ordem_j = 0

while ordem_i <= 0:
    ordem_i = int(input("Qual o número de linhas da sua matriz?\n"))

while ordem_j <= 0:
    ordem_j = int(input("Qual o número de colunas da sua matriz?\n"))
    
Matriz = []

for i in range(ordem_i):
    Matriz.append([0]*ordem_j)

    for j in range(ordem_j):
        Matriz[i][j] = randint(0,1000)

print(Matriz)

maior, linha, coluna = MAX(Matriz)
print(f"O maior valor da matriz é {maior}, que está na posição {linha}x{coluna}!")