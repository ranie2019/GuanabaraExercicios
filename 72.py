num = ('zero', 'um', 'dois', 'treis', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
       'dez', 'onze', 'doze', 'treze', 'quatroze', 'quize', 'dezesseis', 'dezessete', 'dezoitos'
       'desenove', 'vinte')
while True:
    n = int(input('Digite um numero ate 20: '))
    if 0 <= n <= 20:
       print(f'Voce digitou o Numero {num[n]}')