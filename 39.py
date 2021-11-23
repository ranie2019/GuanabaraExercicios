# Alistamento Militar

from datetime import date

atual = date.today().year
nasc = int(input('ano de nascimento: '))
idade = atual - nasc
print(f'quem nasceu em {nasc} tem {idade} em {atual}')
if idade == 18:
    print("voce tem que se alistar imediatamente")
elif idade < 18:
    saldo = 18 - idade
    print(f'ainda falta {saldo} anos para o alistamento')
    ano = atual + saldo
    print(f'seu alistamento sera em {ano}')
elif idade > 18:
    saldo = idade - 18
    print(f'voce ja deveria ter se alistado a {saldo} anos')
    ano = atual - saldo
    print(f'seu alistamento foi em {ano}')
