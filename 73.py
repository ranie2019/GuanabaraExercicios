times = ('Atlético-MG', 'Flamengo', 'São Paulo', 'Internacional', 'Fluminense', 'Palmeiras',
        'Santos', 'Grêmio', 'Fortaleza', 'Corinthians', 'Athletico-PR', 'Bahia', 'Atlético-GO',
        'Bragantino', 'Ceará')
print('-*' * 15)
print(f'Lista de times do Brasileirao 2020 {times}')
print('-*' * 15)

print(f'Os 5 Primeiros Colocados\n{times[0:5]}')
print('-*' * 15)
print(f'Os 4 Ultimos Colocados\n{times[-4:]}')
print('-*' * 15)
print(f'Os Times em Ordem Alfabeticas\n{sorted(times)}')
print('-*' * 15)
print(f'O Palmeiras esta na {times.index("Palmeiras")+1}° Posicao')