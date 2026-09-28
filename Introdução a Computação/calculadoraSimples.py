#Segundo código, feito na aula 3 :) (25/03/2025)

"""
#Exercício 1
print("Vamos fazer cálculos simples entre dois números inteiros!")

n1 = int(input("Digite aqui o valor do 1º operando: "))
n2 = int(input("Digite aqui o valor do 2º operando: "))

print("Agora, escolha uma das operações possíveis a seguir:")
print("1) Somar")
print("2) Subtrair")
print("3) Multiplicar")
print("4) Dividir")

operação = int(input("Qual a sua escolha? "))

if operação == 1 :
    print(n1 + n2)

if operação == 2 :
    print (n1 - n2)

if operação == 3 :
    print (n1 * n2)

if operação == 4 :
    print(n1 / n2)
    
print("Fim =)")
"""

#Exercício 2
print("Vamos fazer cálculos simples entre dois números inteiros!")

n1 = int(input("Digite aqui o valor do 1º operando: "))
n2 = int(input("Digite aqui o valor do 2º operando: "))

print("Agora, escolha uma das operações possíveis a seguir:")
print("1) Somar")
print("2) Subtrair")
print("3) Multiplicar")
print("4) Dividir")

operação = (input("Qual a sua escolha? "))

if operação == '1' or operação == '1)' or operação == 'Somar' or operação == 'somar' or operação == '1) Somar':
    print("O resultado é: ", n1 + n2)

elif operação == '2' or operação == '2)' or operação == 'Subtrair' or operação == 'subtrair' or operação == '2) Subtrair':
    print ("O resultado é: ", n1 - n2)

elif operação == '3' or operação == '3)' or operação == 'Multiplicar' or operação == 'multiplicar' or operação == '3) Multiplicar':
    print ("O resultado é: ", n1 * n2)

elif operação == '4' or operação == '4)' or operação == 'Dividir' or operação == 'dividir' or operação == '4) Dividir':
    print("O resultado é: ", n1 / n2)
    
print("Fim =)")
