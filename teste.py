print("qual seu nome?")


Nome_Usuario =  input()

print("Bem Vindo",Nome_Usuario,sep="-")

Num_Secreto = 24

Usuario_Entrada = input("Digite sua tentativa ... ")
while True:
    try: 
        Usuario_Entrada = int(Usuario_Entrada)
        break
    except:
        print("Digite um número")
        Usuario_Entrada = input("Digite sua tentantiva...")

tentativas = 3
while (tentativas > 0 ) :
    if Usuario_Entrada ==  0:
        print("Erro no input")

    if Num_Secreto == Usuario_Entrada :
        print("Parabens , Voce Acertou")
        break
    elif Num_Secreto < Usuario_Entrada:
        print("chute muito alto")
        tentativas = tentativas - 1;
        print(tentativas)
        Usuario_Entrada = input("Digite sua tentativa ... ")
        Usuario_Entrada = int(Usuario_Entrada)
        if Num_Secreto == Usuario_Entrada:
            print("Parabens, voce acertou")
    elif Num_Secreto > Usuario_Entrada:
        print("chute muito baixo")
        tentativas = tentativas - 1;
        print(tentativas)
        Usuario_Entrada = input("Digite sua tentativa ... ")
        Usuario_Entrada = int(Usuario_Entrada)
        if Num_Secreto == Usuario_Entrada:
            print("Parabens, voce acertou")

              



        
