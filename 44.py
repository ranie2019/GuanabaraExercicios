# Gerenciador de Pagamentos

print('{:*^40}'.format(' Lojas R.A '))
preco = float(input('preço das compras R$: '))
print('''formas de Pagamento
[1] A Vista Dinheiro / Cheque
[2] A Vista Cartao 
[3] 2X No Cartao
[4] 3X Ou Mais No Cartao''')
opcao = int(input('Qual Sua Opcao: '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print(f'Sua Parcela em 2X de R$ {parcela :.2f} Sem Juros')
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totalParcela = int(input('Quantas Parcelas? '))
    parcela = total / totalParcela
    print(f'Sua Compra Sera Parcelada em {totalParcela} X De R$ {parcela :.2f} Com Juros')
else:
    total = preco
    print('Opcao Invalida. Tente Novamente!')
print(f'Sua Compra de R${preco :.2f} Vai Custar R${total :.2f} no final')
