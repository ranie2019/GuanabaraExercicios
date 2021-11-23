# Aprovando Empréstimo

casa = float(input('valor da casa R$ '))
salario = float(input('salario R$ '))
anos = int(input('quantos anos financiando? '))

prestacao = casa / (anos * 12)
minimo = salario * 30 / 100

print(f'Para pagar uma casa de R${casa:.2f} em {anos} Anos')
print(f'A prestacao sera de R${prestacao:.2f}')

if prestacao <= minimo:
    print('Emprestimo Aprovado')
else:
    print('Emprestimo Negado')
