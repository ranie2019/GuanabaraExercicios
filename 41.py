# Alistamento Militar
from datetime import date

atual = date.today().year
nasc = int(input('Ano de Nascimento: '))
idade = atual - nasc
print(f'Quem Nasceu Em {nasc} tem anos em {idade} Em {atual}')
if idade == 18:
    print('voce Tem Que Se Alistar Imediatamente')
elif idade < 18:
    saldo = 18 - idade
    print(f'Ainda Falta {saldo}')
elif idade > 18:
    saldo = idade - 18
    print(f'Voce Ja Deveria Ter Se Alistado Ha {saldo} Anos')
