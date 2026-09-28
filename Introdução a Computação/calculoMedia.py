'''
#Criamos uma função através da sintaxe "def nome_da_função():"
def calcular_media(a,b):
	med= (a+b)/2
	print=(f'A média entre {a} e {b} = {med}')
	

#Programa principal
x = int(input("Digite o primeiro valor "))
y = int(input("Digite o segundo valor"))
calcular_media(x,y)                         #Chamamos a função
print("Fim de Programa")


'''

'''

#Criamos uma função através da sintaxe "def nome_da_função():"
def calcular_media(a,b):
	med= (a+b)/2
	return med              #temos que colocar essa função de retorno para que o "programa" saiba que deve guardar a informação

#Programa principal
x = int(input("Digite o primeiro valor "))
y = int(input("Digite o segundo valor"))
media = calcular_media(x,y)                         #Guardamos em algum lugar
print=(f'A média entre {x} e {y} = {media}')
print("Fim de Programa")

'''

def calcular_media(a,b):
	return (a+b)/2
	
x = int(input("Digite o primeiro valor "))
y = int(input("Digite o segundo valor "))
print(f'A média entre {x} e {y} = {calcular_media(x,y)}') #aí não gravamos nenhuma informação, apenas pegamos o último valor do retorno
print("Fim de Programa")