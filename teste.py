import random
print("qual seu nome?")


Nome_Usuario =  input()

print("Bem Vindo",Nome_Usuario,sep="-")

Num_Secreto = random.randint(1,100)
print(Num_Secreto)

print("Selecione seu nível de dificuldade")
print("fácil (1), médio(2), difícil(3)")
Nivel_Dificuldade = input("Dificuldade")
while True:
    try: 
        Nivel_Dificuldade = int(Nivel_Dificuldade)
        break
    except:  
          print("Digite 1 para fácil, 2 para médio e 3 para difícil")


Usuario_Entrada = input("Digite sua tentativa ... ")
while True:
    try: 
        Usuario_Entrada = int(Usuario_Entrada)
        break
    except:
        print("Digite um número")
        Usuario_Entrada = input("Digite sua tentantiva...")

if Nivel_Dificuldade == 1:
    tentativas= 5
elif Nivel_Dificuldade == 2:
    tentativas = 4
elif Nivel_Dificuldade == 3:
    tentativas = 3
restantes = 1                    
while (restantes < tentativas ) :
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

              



        
