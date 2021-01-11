palavras = ('crie', 'programa', 'tenha', 'tupla', 'varias', 'palavras', 'acentos',
            'depois', 'mostrar', 'vogais', 'exercicio', 'python')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos as Vogais ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=', ')