print('Gerador de PA')
print('-=' * 18)
primeiro = int(input('1° termo: '))
rasao = int(input('Rasao da PA: '))
termo = primeiro
conta = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while conta <= total:
        print(f'{termo} ', end=" ")
        termo += rasao
        conta += 1
    print('Pausa')
    mais = int(input('Quantos termos vc que mostrar a mais? '))
print(f'Proguecao finalizado com {total} termos mostrados')