listnum = []
max = 0
min = 0
for c in range(0,5):
    listnum.append(int(input(f'Digite um valor na posicao {c}: ')))
    if c == 0:
        max = min = listnum[c]
    else:
        if listnum[c] > max:
            max = listnum[c]
        if listnum[c] < min:
            min = listnum[c]
print('=-' * 30)
print(f'voce digitou os valores {listnum}')
print(f'o maior valor foi {max} nas posicoes ', end='')
for i, v in enumerate(listnum):
    if v == max:
        print(f'{i}.. ', end='')
print()
print(f'o menor valor foi {min} nas posicoes ', end='')
for i, v in enumerate(listnum):
    if v == min:
        print(f'{i}.. ', end='')
print()
