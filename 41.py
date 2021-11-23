# Classificando Atletas

from datetime import date

atual = date.today().year
nasc = int(input('digite seu ano de nascimento: '))
idade = atual - nasc

if idade <= 9:
    print(f'voce tem {idade} anos \nvoce e mirim')

elif 9 < idade <= 14:
    print(f'voce tem {idade} anos \nvoce e infantil')

elif 14 < idade <= 19:
    print(f'voce tem {idade} anos \nvoce e junior')

elif 19 < idade <= 25:
    print(f'voce tem {idade} anos \nvoce e senior')

else:
    print(f'voce tem {idade} anos \nvoce e master')