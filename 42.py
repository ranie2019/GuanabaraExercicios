# Analisando Triângulos v2.0

r1 = float(input('1° segmento: '))
r2 = float(input('2° segmento: '))
r3 = float(input('3° segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima Podem formar um Triângulo', end=' ')
    if r1 == r2 == r3:
        print('Equilatero!')
    if r1 != r2 != r3:
        print('Escaleno!')
    else:
        print('Isosceles!')
else:
    print('os segmentos acima nao podem formar um Triângulo')
