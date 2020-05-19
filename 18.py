# Seno, Cosseno e Tangente

from math import radians, sin, cos, tan
an = float(input('digite o angulo que voce deseja: '))
seno = sin(radians(an))
print(f'o angulo de {an} tem o seno de {seno:.2f}')
cosseno = cos(radians(an))
print(f'o angulo de {an} tem o cosseno de {cosseno:.2f}')
tangente = tan(radians(an))
print(f'o angulo de {an} tem o tangente de {tangente:.2f}')