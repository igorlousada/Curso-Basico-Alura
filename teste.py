import random

print("qual seu nome?")


Nome_Usuario =  input()

print("Bem Vindo",Nome_Usuario,sep="-")

Num_Secreto = random.randint(1,100)

Usuario_Entrada = input("Digite sua tentativa ... ")
while True:
    try: 
        Usuario_Entrada = int(Usuario_Entrada)
        break
    except:
        print("Digite um número")
        Usuario_Entrada = input("Digite sua tentantiva...")

tentativas = 3
restantes  = 1
while (restantes < 3 ) :
    print("rodada {} de {}".format(restantes,tentativas))
    if Usuario_Entrada ==  0:
        print("Erro no input")

    if Num_Secreto == Usuario_Entrada :
        print("Parabens , Voce Acertou")
        break
    elif Num_Secreto < Usuario_Entrada:
        print("chute muito alto")
        restantes = restantes + 1;
        Usuario_Entrada = input("Digite sua tentativa ... ")
        Usuario_Entrada = int(Usuario_Entrada)
        if Num_Secreto == Usuario_Entrada:
            print("Parabens, voce acertou")
    elif Num_Secreto > Usuario_Entrada:
        print("chute muito baixo")
        restantes = restantes + 1;
        Usuario_Entrada = input("Digite sua tentativa ... ")
        Usuario_Entrada = int(Usuario_Entrada)
        if Num_Secreto == Usuario_Entrada:
            print("Parabens, voce acertou")

              



        
