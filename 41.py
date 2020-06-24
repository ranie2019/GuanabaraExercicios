# Classificando Atletas

from datetime import date

atual = date.today().year
nasc = int(input('digite seu ano de nascimento: '))
idade = atual - nasc

if idade <= 9:
    print(f'voce tem {idade} anos \nvoce e mirim')

elif idade > 9 and idade <= 14:
    print(f'voce tem {idade} anos \nvoce e infantil')

elif idade > 14 and idade <= 19:
    print(f'voce tem {idade} anos \nvoce e junior')

elif idade > 19 and idade <= 25:
    print(f'voce tem {idade} anos \nvoce e senior')

else:
    print(f'voce tem {idade} anos \nvoce e master')