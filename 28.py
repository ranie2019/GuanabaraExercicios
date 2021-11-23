# #028 - Jogo da Adivinhação v.1.0

from random import randint
from time import sleep
computador = randint(0, 5)

print('-=' * 24)
print('vou pensar um um numero de 0 a 5 tente adivinhar')
print('-=' * 24)

nu = int(input('em que numero eu pensei? '))
print('Processando.')
sleep(1)
print('Processando..')
sleep(1)
print('Processando...')
sleep(1)
if nu == computador:
    print('parabens voce ganhou')
else:
    print(f'voce perdeu eu pensei no numero {computador} e nao no {nu}')
