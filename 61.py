print('Gerador de PA')
print('-=' * 18)
primeiro = int(input('1° termo: '))
rasao = int(input('Rasao da PA: '))
termo = primeiro
conta = 1
while conta <= 10:
    print(f'{termo} ', end=" ")
    termo += rasao
    conta += 1
print('Fim')