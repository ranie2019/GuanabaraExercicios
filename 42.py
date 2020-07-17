# Analisando Triângulos v2.0

r1 = float(input('1° segimento: '))
r2 = float(input('2° segimento: '))
r3 = float(input('3° segimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima Podem formar um Triângulo', end=' ')
    if r1 == r2 == r3:
        print('Equilatero!')
    if r1 != r2 != r3:
        print('Escaleno!')
    else:
        print('Isosceles!')
else:
    print('os segmentos acima nao podem formar um Triâng')