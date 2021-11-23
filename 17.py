# Catetos e Hipotenusa
from math import hypot
co = float(input('comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adjacente: '))
soma = (co ** 2 + ca ** 2) ** (1/2)
somas = hypot(co, ca)
print(f'a hipotenusa vai medir {somas:.2f}')
