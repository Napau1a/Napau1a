#Primeiro código =) Feito na aula 02

#Dados dos retângulos
LADO_1 = float(input('Digite o valor do Lado 1 = '))
LADO_2 = float(input('Digite o valor do Lado 2 = '))
LADO_3 = float(input('Digite o valor do Lado 3 = '))
LADO_4 = float(input('Digite o valor do Lado 4 = '))
LADO_5 = float(input('Digite o valor do Lado 5 = '))
LADO_6 = float(input('Digite o valor do Lado 6 = '))

#Cálculo de área
ÁREA1 = LADO_1 * LADO_2
ÁREA2 = (LADO_4 + (LADO_2 - LADO_6)) * ((LADO_1 - LADO_3) + LADO_5)
ÁREA3 = (LADO_2 - LADO_6) * (LADO_1 - LADO_3)
ÁREA = ÁREA1 + ÁREA2 - ÁREA3


#Mostrar resultado
print ("Área total da figura",ÁREA)