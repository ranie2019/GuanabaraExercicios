from random import randint
v = 0
while True:
    jogador = int(input('Digite um Valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = " "
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print(f'Voce Jogou {jogador} e o Computador {computador}. Total de {total}', end=' ')
    print('Deu Par' if total % 2 == 0 else 'Deu Impar')
    if tipo == 'P':
        if total % 2 == 0:
            print('Voce Venceu')
            v += 1
        else:
            print('Voce Perdeu')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Voce Venceu')
            v += 1
        else:
            print('Voce Perdeu')
            break
    print('Vamos Jogar Novamente')
print(f'Game Over Voce Venceu {v} Vezes.')