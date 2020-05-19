# Primeiro e último nome de uma pessoa

n = str(input('digite o seu nome completo: '))
nome = n.split()
print('muito prazer em te conhecer')
print(f'seu primeiro nome e {nome[0]} ')
print(f'seu ultimo nome e {nome[len(nome)-1]}')
