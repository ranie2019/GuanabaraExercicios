tot18 = toth = totm20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        toth += 1
    if sexo == 'F' and idade < 20:
        totm20 += 1
    resposta = ' '
    while resposta not in 'S/N':
        resposta = str(input('Quer Continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
print(f'Total de Pessoas Com mais de 18 anos: {tot18}')
print(f'Ao todo temos {toth} Homens Cadastros')
print(f'E temos {totm20} Mulheres com Menos de 20 anos')