peso=float(input('Digite o peso: '))
altura=float(input('Digite a altura: '))
imc=peso/(altura*altura)

print(f'IMC: {imc}')

if imc>=25:
    print('Acima do peso')
elif imc>=18.5:
    print('Peso normal')
else:
    print('Abaixo do peso')