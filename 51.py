p = int(input('1° termo: '))
r = int(input('razao: '))
d = p + (10 - 1) * r
for c in range(p, d, r):
    print(f'{c}', end=' > ')
print('Acabou')