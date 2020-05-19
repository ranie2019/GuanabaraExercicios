# Primeira e última ocorrência de uma string

frase = str(input('digite uma frase: ')).strip().upper()
print('a letra A aparece {} na frase'.format(frase.count('A')))
print('a primeira letra A pareceu na posicao {}'.format(frase.find('A')+1))
print('a primeira letra A pareceu na posicao {}'.format(frase.rfind('A')+1))