peso = float(input('qual o seu peso? (KG): '))
altura = float(input('qual sua altura? (m): '))
imc = peso / (altura ** 2)

print(f'O Seu IMC e de {imc:.2f}')

if imc <= 18.5:
    print('Voce ta Abaixo do Peso')
elif 18.5 <= imc < 24.9:
    print('Seu Peso é Normal')
elif 25 <= imc < 29.9:
    print('Voce ta Com Sobrepeso')
elif 30 <= imc < 34.9:
    print('Voce ta Com Obesidade Gral 1')
elif 35 <= imc < 39.9:
    print('Voce ta Com Obesidade Gral 2')
else:
    print('Voce ta Com Obesidade Gral 3')
