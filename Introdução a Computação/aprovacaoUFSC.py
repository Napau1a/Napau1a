# Introdução
print("Bem-vinde à calculadora do sistema de notas da UFSC! 😊")
print("PS.: Máximo de duas notas!")
print("Como deves imaginar, vou precisar de alguns dados!")


# Receber notas
P1 = float(input("Como você foi na primeira prova? "))
P2 = float(input("Como você foi na segunda prova? "))


# Fazer média
Média = (P1+P2)/2


# Arredondamento
Arredondamento = Média%1 
""
if Arredondamento >= 0 and Arredondamento <= 0.24 :
    Nota = Média - Arredondamento

elif Arredondamento >= 0.25 and Arredondamento <= 0.74 :
    Nota = Média - Arredondamento + 0.5

elif Arredondamento >= 0.75 and Arredondamento <= 1.00 :
    Nota = Média - Arredondamento + 1.0


# Checagem para Rec

if Nota <= 2.9 :
    print("Infelizmente, você não alcançou a média suficiente para ter o direito à recuperação e não foi aprovade nesta disciplina 😢. Mas não desista, tente novamente no próximo semestre e procure a ajuda dos monitores, ou professores em seus horários de atendimento ou e-mail 🤗")

elif Nota >= 3 and Nota < 6.0 :
    print("Ok... A sua média foi de ", Nota, "infelizmente você ainda não foi aprovade, mas precisamos verificar mais umas coisinhas...")
    freq = int(input("Considerando a métrica da UFSC de 0 a 100, qual foi a sua frequência nas aulas desse semestre? "))

    if freq < 75 :
        print("😞 Você tem frequência insuficiente (FI) e, portanto, não tem direito à recuperação e está reprovade 😢. Mas não desista, tente novamente no próximo semestre e procure a ajuda dos monitores, ou professores em seus horários de atendimento ou e-mail 🤗")

    elif freq >= 75 :
        print("Bom sinal! Sua frequência é suficiente 🤗! Isto, com a sua média sendo ", Nota, "lhe concede o direito a recuperação! Boa sorte e bons estudos! Não esqueça de pedir ajuda aos monitores da disciplina e aos professores 😉")
        print("Volte com o resultado da sua recuperação!")

        Rec = float(input("Qual a nota obtida em sua prova de recuperação? "))
        MédiaRec = (Nota+Rec)/2

        #Arredondamento com Rec
        ArredondamentoRec = MédiaRec%1

        if ArredondamentoRec >= 0.0 and ArredondamentoRec <= 0.24 :
            Final = MédiaRec - ArredondamentoRec

        elif ArredondamentoRec >= 0.25 and ArredondamentoRec <= 0.74 :
            Final = MédiaRec - ArredondamentoRec + 0.5
        
        elif ArredondamentoRec >= 0.75 and ArredondamentoRec <= 1.00 :
            Final = MédiaRec - ArredondamentoRec + 1.00
        
        if Final >= 6 :
            print("🎉 Parabéns!! Você foi aprovade ✨!!")
        
        elif Final < 6 :
            print("Não foi dessa vez 😕... Mas não desista! Tente novamente no próximo semestre e procure a ajuda dos monitores, ou professores em seus horários de atendimento ou e-mail 🤗")


elif Nota >= 6.0 :
    print("😁 Muito bem! Você obteve a média necessária para aprovação! A sua média foi de ", Nota,"!")
    print("Agora, para checar sua frequência tudo bem? 👀")

    freq = int(input("Considerando a métrica da UFSC de 0 a 100, qual foi a sua frequência nas aulas desse semestre? "))

    if freq < 75 :
        print("😞 Você tem frequência insuficiente (FI). Infelizmente, mesmo atingindo a nota necessária, sem a frequência esperada, você não está aprovade.")
        print("Lembre-se que você está numa modalidade de ensino presencial e que, se não justificadas, suas faltas podem lhe prejudicar 😟")
        print("Mas não desista! Tente novamente no próximo semestre, se continuar assim e aumentar a frequência nas aulas, você terá tudo o que precisa para a aprovação! 🤗")
        
    if freq >= 75 :
           print("🎉 Parabéns!! Você foi aprovade ✨!!")     
