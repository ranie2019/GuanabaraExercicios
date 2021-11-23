# Aquele clássico da Média

n1 = float(input('1° nota: '))
n2 = float(input('2° nota: '))
n3 = float(input('3° nota: '))
n4 = float(input('4° nota: '))

soma = (n1 + n2 + n3 + n4) / 4

if soma >= 7:
    print(f'a media foi {soma:.2f}\no aluno esta aprovado')
elif soma > 5 <= 6.9:
    print(f'a media foi {soma:.2f}\no aluno esta de recuperacao')
else:
    print(f'a media foi {soma:.2f}\no aluno esta reprovado')
    print(f'')
