# Ano Bissexto

from datetime import date
ano = int(input('que ano voce quer analisar? \ncoloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'o ano {ano} e bissexto')
else:
    print(f'o ano de {ano} nao e bissexto')