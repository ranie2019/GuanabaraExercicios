total = totmil = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do Produto '))
    preco = float(input('Preco R$ '))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer Continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('Fim Do Programa '))
print(f'O total de Compras foi R$ {total}')
print(f'Temos {totmil} Produtos Custando mais de mil Reais')
print(f'O Produto mais Barato foi a {barato} e Custa R${menor:.2f}')