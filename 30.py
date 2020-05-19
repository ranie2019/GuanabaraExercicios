# Par ou Ímpar?

numero = int(input('digite um numero: '))
soma = numero % 2
if soma == 0:
    print(f'o numero {numero} e par ')
else:
    print(f'o numero {numero} e impar')