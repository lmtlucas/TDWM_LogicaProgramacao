#idade=int(input('Digite sua idade: '))

#if idade >= 18:
#    print(f'Com {idade} anos. Você é maior de idade')
#else:
#    print('Você é menor de idade')
###################################################
#nota=float(input('Digite sua nota: '))

#if nota==10:
 #   print(f'Tirou {nota}. Parabéns! Aprovadissimo!')
#elif nota>=7:
#    print(f'Tirou {nota}. Aprovado!')
#elif nota>=5:
 #   print(f'Tirou {nota}. Recuperação.')
#else:
 #   print(f'Tirou {nota}. Reprovado')
 ##################################################################


velocidade=float(input('insira a velocidade atingida: '))

if velocidade>=300:
    print('esse veiculo é um avião')
elif velocidade >=100:
    print('o veiculo é um carro')
elif velocidade >=30:
    print('o veiculo é uma moto')
elif velocidade>=5:
    print('o veiculo é uma bicicleta')
else:

    print('sem veiculo')
