print('=' * 30)
print('{:^30}'.format('BANCO R.A'))
print('=' * 30)

valor = int(input('Digite o valor que voce que sacar R$ '))
total = valor
cedula = 200
totalcedula = 0

while True:
    if total >= cedula:
        total -= cedula
        totalcedula += 1
    else:
        if totalcedula > 0:
            print(f'Total De {totalcedula} Cedulas De R$ {cedula}')
        if cedula == 200:
            cedula = 100
        elif cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula == 2
        totalcedula = 0
        if total == 0:
            break
print('=' * 30)
print('Obrigado Volte Sempre')