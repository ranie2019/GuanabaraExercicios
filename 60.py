from math import factorial
n = int(input('Digite um numero: '))
f = factorial(n)
print(f'O fatorial de {n} e {f}')

####################################

c = n
f = 1
print(f'calculando {c}! =', end=" ")
while c > 0:
    print(f'{c}', end="")
    print(' x ' if c > 1 else " = ", end='')
    f *= c
    c -= 1
print(f'{f}')