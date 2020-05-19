# Custo da Viagem

viagem = int(input('qual a distancia da viagem em KM? '))

if viagem <= 200:
    preco = viagem * 0.50
    print(f'o valor da viagem e de R${viagem:.2f}')

else:
    preco = viagem * 0.45
    print(f'o valor da viagem e de R${preco:.2f}')