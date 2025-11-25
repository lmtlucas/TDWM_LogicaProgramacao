total = 0
quant_digitada = 0

while quant_digitada <5:
    n = float(input('Digite um numero: '))
    total += n
    quant_digitada +=1

print(f'A soma dos numeros digitados é: {total}')