num = int(input('digite um numero: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[32m', end=' ')
        tot +=1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=" ")
print(f'\n\033[mO numero {num} foi divisivel {tot} vezes')
if tot == 2:
    print(f'O {num} e primo')
else:
    print(f'o {num} nao e primo')