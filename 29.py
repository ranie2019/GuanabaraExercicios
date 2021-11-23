# Radar eletrônico

velocidade = float(input('qual a velocidade do carro: '))
if velocidade > 120:
    print('multado por exceder o limite permitido de 120KM/H')
    multa = (velocidade - 120) * 7
    print(f'voce deve pagar uma multa de {multa}')
print('tenha um bom dia e va com seguranca!')
