listagem = ('lapis', 1.75, 'caderno', 15.90, 'borracha', 1.00, 'estojo', 5.00, 'trasferidor', 4.50,
            'compasso', 9.99, 'mochila', 150.00, 'caneta', 2.50, 'livros', 35.00)
print('-' * 23)
print(f'{"Lista de Precos":^23}')
print('-' * 23)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<15}', end='')
    else:
        print(f'R${listagem[pos]:>6.2f}')
print('-' * 23)