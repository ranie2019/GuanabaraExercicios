valor = []
while True:
    valor.append(int(input('digite um valor: ')))
    resp = str(input('que continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-='*20)
print(f'voce digitou {len(valor)} elementos')
valor.sort(reverse=True)
print(f'os valores em ordem decrescente sao {valor}')
if 5 in valor:
    print('o valor 5 esta na lista')
else:
    print('o valor 5 nao esta na lista')
