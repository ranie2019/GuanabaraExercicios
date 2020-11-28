from random import randint
numeros = (randint(1, 5), randint(1, 10), randint(1, 15), randint(1, 20), randint(1, 25), )
print('Eu Sortei os valores: ', end='')
for n in numeros:
    print(f'{n}', end=" ")
print(f'\nO maior valor foi {max(numeros)}')
print(f'O menor valor foi {min(numeros)}')