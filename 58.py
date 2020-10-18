from random import randint
computador = randint(0, 10)
print('')
print('Sou o Seu Computador... Acabei de Pensar em um Numero Entre 0 e 10.')
print('Tente Adivinhar se Voce For Capaz')

acertou = False
palpite = 0

while not acertou:
    jogador = int(input('Qual o seu Palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais')
        elif jogador > computador:
            print('Menos... Tente Mais')
print(f'Acertou! em {palpite} Tentativas')