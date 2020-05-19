# Analisando Triângulo v1.0

print('-=' * 15)
print('Analizador De Triangulos')
print('-=' * 15)

t1 = float(input('1° Segmento: '))
t2 = float(input('2° Segmento: '))
t3 = float(input('3° Segmento: '))

if t1 < t2 + t3 and t2 < t1 + t3 and t3 < t1 + t2:
    print('Os Segmentos Podem Formar Um Triangulo')
else:
    print('Os Segmentos Nao Podem Formar Um Triangulo')
