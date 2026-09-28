'''(IMC= massa em Kg/altura em metros elevado ao quadrado)
'''

def calculadora(a,b):
    return (a/(b**2))

m = float(input('Digite aqui a sua massa em Kg: '))
h = float(input('Digite aqui o valor da sua altura, em metros: '))

if calculadora(m,h) <= 18.5 :
    print(f"O seu IMC foi calculado em: {calculadora(m,h):.1f}. Infelizmente sua situação é: abaixo do peso ideal. Mas não se preocupe, com acompanhamento correto você poderá se manter saudável :)")

elif calculadora(m,h) < 25 :
    print(f"O seu IMC foi calculado em: {calculadora(m,h):.1f}. Que ótimo! Sua situação é: saudável.")

elif calculadora(m,h) < 30 :
    print(f"O seu IMC foi calculado em: {calculadora(m,h):.1f}. Infelizmente sua situação é: peso em excesso. Mas não se preocupe, com acompanhamento correto você poderá se manter saudável :)")

elif calculadora(m,h) < 35 :
    print(f"O seu IMC foi calculado em: {calculadora(m,h):.1f}. Infelizmente sua situação é: Obesidade Grau I. Mas não se preocupe, com acompanhamento correto você poderá se manter saudável :)")

elif calculadora(m,h) < 40 :
    print(f"O seu IMC foi calculado em: {calculadora(m,h):.1f}. Infelizmente sua situação é: Obesidade Grau II (severa). Mas não se preocupe, com acompanhamento correto você poderá se manter saudável :)")

elif calculadora(m,h)>= 40 :
    print(f"O seu IMC foi calculado em: {calculadora(m,h):.1f}. Infelizmente sua situação é: Obesidade Grau III (mórbida). Mas não se preocupe, com acompanhamento correto você poderá se manter saudável e reverter esse quadro :)")