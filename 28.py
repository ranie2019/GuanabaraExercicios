# #028 - Jogo da Adivinhação v.1.0

from random import randint
from time import sleep
computador = randint(0,5) # faz o cumputador pensar

print('-=' * 24)
print('vou pensar um um numero de 0 a 5 tente adivinhar')
print('-=' * 24)

nu = int(input('emq ue numero eu pensei? '))
print('precessando...')
sleep(2)
if nu == computador:
    print('parabens voce ganhou')
else:
    print(f'voce perdeu eu pensei no numero {computador} e nao no {nu}')