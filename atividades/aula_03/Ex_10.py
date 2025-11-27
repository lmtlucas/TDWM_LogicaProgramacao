velocidadeDoCarro=float(input('Informe a velocidade do carro em km/h: '))
velocidadeMaximaPermitida=80


print(f'Velocidade do motorista: {velocidadeDoCarro} km/h')
print(f'Velocidade máxima permitida: {velocidadeMaximaPermitida} km/h')
if velocidadeDoCarro>velocidadeMaximaPermitida+20:
    print('O motorista cometeu infração grave\nReceberá 7 pontos na carteira')
elif velocidadeDoCarro>=velocidadeMaximaPermitida+11:
    print('O motorista cometeu infração média\nReceberá 4 pontos na carteira')
elif velocidadeDoCarro>velocidadeMaximaPermitida:
    print('O motorista cometeu infração leve\nReceberá 3 pontos na carteira')
else:
    print('O motorista não cometeu infração\n0 pontos na carteira')