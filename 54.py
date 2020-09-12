from datetime import date
atual = date.today().year
tmaior = 0
tmenor = 0
for pes in range(1, 8):
    nas = int(input(f'Em que ano a {pes}° nasceu? '))
    idade: atual = atual - nas
    if idade >= 18:
        tmaior += 1
    else:
       tmenor += 1
print(f'Ao todo tivemos {tmaior} Maiores de idade \ne {tmenor} Menores de Idade')