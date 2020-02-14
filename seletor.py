import adivinhacao
import forca
import random

print("Bem-vindo")


jogo = input("Qual jogo deseja jogar? (1) adivinhação (2)forca")

while True:
    try:
        jogo = int(jogo)
        break
    except:
        print("Por favor, digite (1) para adivinhação e (2) para forca")
if jogo == 1:
    
    adivinhacao.jogar()

if jogo == 2:
    
    forca.jogar()