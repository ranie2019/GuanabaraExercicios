numero = (int(input('digite um numero: ')),
          int(input('digite um numero: ')),
          int(input('digite um numero: ')),
          int(input('digite um numero: ')))
print(f'voce digitou {numero}')
print(f'O valor 9 apareceu {numero.count(9)} Vezes')
if 3 in numero:
    print(f'O valor 3 apareceu na {numero.index(3)+1}° Posicao')
else:
    print('O valor 3 nao foi Digitado')
print('Os valores Pares Foram: ', end='')
for n in numero:
    if n % 2 == 0:
        print(n, end=', ')