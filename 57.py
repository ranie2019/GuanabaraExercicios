print('')
print('Digite M para Masculino e F para Feminino')
sexo = str(input('digite o seu sexo: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados Invalidos. Por Favor Informe Seu Sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} Registrado Com Sucesso')