numeros = list()
while True:
    n = int(input('digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor Adicionado com Sucesso: ')
    else:
        print('Valor Duplicado! nao Vou Adicionar...')
    r = str(input('Quer Continuar? [S/N] '))
    if r in 'Nn':
        break
print('=-' * 30)
print(f'Voce Digitou os Valores {numeros}')
