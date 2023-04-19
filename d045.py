from random import randint
from time import sleep
items = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print("""Suas opções:
[ 0 ] Pedra 
[ 1 ] Papel
[ 2 ] Tesoura""")
jogador = int(input("Qual a sua jogada? "))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!")
print("-=" * 11)
print(f"O jogador jogou {items[jogador]}")
print(f"O computador jogou {items[computador]}")
print("-=" * 11)
if computador == 0:
    if jogador == 0:
        print("Empate!")

    elif jogador == 1:
        print("Você Ganhou!")

    elif jogador == 2:
        print("Você Perdeu!")
    else:
        print("Jogada Invalida!")

elif computador == 1:
    if jogador == 0:
        print("Você Perdeu!")
    elif jogador == 1:
        print("Empate")
    elif jogador == 2:
        print("Você Ganhou")
    else:
        print("Jogada Invalida!")

elif computador == 2:
    if jogador == 0:
        print("Você Ganhou!")
    elif jogador == 1:
        print("Você Perdeu")
    elif jogador == 2:
        print("Empate")
    else:
        print("Jogada Invalida!")

