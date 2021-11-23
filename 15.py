# Aluguel de Carros

dias = float(input('quantidade de dias '))
km = int(input('Quantidade de KM Percorrido: '))
pago = dias * 60 + km * 0.15

print(f'o total a pagar e de R${pago:.2f}')
