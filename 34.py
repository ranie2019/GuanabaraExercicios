# Aumentos múltiplos

salario = float(input('qual o seu salario? '))
if salario <= 1200:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print(f'o salario de {salario:.2f} vai para {novo:.2f}')