# Criando uma Calculadora

n1 = int(input('1° numero: '))
n2 = int(input('2° numero: '))
opcao = 0

print('''[1] somar
[2] multiplicar
[3] menos
[4] divisão8
5''')
opcao = int(input('qual sua opção? '))
if opcao == 1:
    soma = n1 + n2
    print(f'o resultado e {soma}')

elif opcao ==2:
    multiplicar = n1 * n2
    print(f'o resultado e {multiplicar}')

elif opcao == 3:
    menos = n1 - n2
    print(f'o resultado e {menos}')

elif opcao == 4:
    divisão = n1 / n2
    print(f'o resultado e {divisão}')

else:
    print('opção invalida. Tente de novo')

print('fim do programa')
