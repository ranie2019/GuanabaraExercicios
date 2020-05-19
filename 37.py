# Conversor de Bases Numéricas

n = int(input('digite um numero: '))
print('''escolha a opcao
1 - Binario
2 - Octal
3 - Hexadecimal''')
opcao = int(input('sua opcao: '))

if opcao == 1:
    print(f'{n} convertido para Binario e igual a {bin(n)[2:]}')
elif opcao == 2:
    print(f'{n} convertido para Octal e igual a {oct(n)[2:]}')
elif opcao == 3:
    print(f'{n} convertido para Hexadecimal e igual a {hex(n)[2:]}')
else:
    print('opcao invalida')