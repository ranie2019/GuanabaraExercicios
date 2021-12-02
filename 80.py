lista = []
for l in range(0, 5):
    v = int(input('Digite um valor: '))
    if l == 0 or v > lista[-1]:
        lista.append(v)
        print(f'Adicionado ao Final da Lista')
    else:
        pos = 0
        while pos < len(lista):
            if v <= lista[pos]:
                lista.insert(pos, v)
                print(f'Adicionado na posicao {pos}')
                break
            pos += 1
print('-='*30)
print(f'os valores digitados em ordem foram {lista}')
