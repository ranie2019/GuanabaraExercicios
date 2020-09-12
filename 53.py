frase = str(input('Digite Uma Frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print(f'O inverso de: {junto}\né:            {inverso}')
if inverso == junto:
    print('temos um palindromo')
else:
    print('nao e um palindromo')
