from random import randint
from time import sleep
print('GAME: Pedra Papel e Tesoura')
itens = ('Pedra', 'Tesoura', 'Papel')
computador = randint(0, 2)
print('''Suas Opcoes:
[0] Pedra
[1] Tesoura
[2] Papel''')
jogador = int(input('Qual Sua Opcao? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('*' * 12)
print(f'Computador Jogou: {itens[computador]}')
print(f'Voce Jogou: {itens[jogador]}')
print('*' * 12)
if computador == 0: # Computador jogou Pedra
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Computador Ganhou')
    elif jogador == 2:
        print('Voce Ganhou')
    else:
        print('jogada invalida!')
elif computador == 1: # Computador jogou Tesoura
    if jogador == 0:
        print('Voce Ganhou')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Computador Ganhou')
    else:
        print('jogada invalida!')
elif computador == 2: # Computador jogou Papel
    if jogador == 0:
        print('Computador Ganhou')
    elif jogador == 1:
        print('Voce Ganhou')
    elif jogador == 2:
        print('Empate')
    else:
        print('jogada invalida!')