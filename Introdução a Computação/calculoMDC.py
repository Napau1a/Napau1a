print("Vamos calcular o Máximo Divisor Comum entre dois números!")

n = int(input('Digite aqui o primeiro número: '))
m = int(input('Digite aqui o segundo número: '))

if n <= m :
    menor = n
    maior = m

else :
    menor = m
    maior = n

for i in range(menor,1,-1) :
    if menor % i == 0 and maior % i == 0 :
        print(f'O seu Máximo Divisor Comum é: {i}')
        break