# Separando dígitos de um número

nu = int(input('digite um numero: '))
u = nu // 1 % 10
d = nu // 10 % 10
c = nu // 100 % 10
m = nu // 1000 % 10

print(f'analindando o numero {nu}')
print(f'Unidade {u}')
print(f'Dezena {d}')
print(f'Centena {c}')
print(f'Milhar {m}')
