# Analisador de Textos

nome = str(input(' digite o seu nome completo: ')).strip()

print(f'seu nome em maiusculo fica {nome.upper()}')
print(f'seu nome em minusculo e {nome.lower()}')
print('seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('o seu primeiro nome tem {} letras'.format(nome.find(' ')))