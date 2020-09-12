somaidade = 0
mediaidade = 0
maioridadehomen = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print(f'{p}° pessoas')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomen = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomen:
        maioridadehomen = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print(f'A media do grupo e de {mediaidade} anos')
print(f'O Homen Mais velho tem {maioridadehomen} anos e se chama {nomevelho}')
print(f'Ao todo sao {totmulher20} mulheres com menos de 20 anos')
