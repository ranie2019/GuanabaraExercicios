#  Procurando uma string dentro de outra

no = str(input('qual o seu nome completo? ')).strip()

print('seu nome tem silva? {}'.format('silva' in no.lower()))
