# Maior e menor valores
a = int(input('1° valor: '))
b = int(input('2° valor: '))
c = int(input('3° valor: '))
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print(f'o maior numero e {maior}')
print(f'o menor numero e {menor}')
