# Radar eletrônico

velocidade = float(input('qual a velocidade do carro: '))
if velocidade > 80:
    print('multado por exceder o limite permitido de 80KM/H')
    multa = (velocidade - 80) * 7
    print(f'voce deve pagar uma multa de {multa}')
print('tenha um bom dia e va com seguranca!')