numeros = []

numeros.append(float(input('Digite o 1º numero: ')))
numeros.append(float(input('Digite o 2º numero: ')))
numeros.append(float(input('Digite o 3º numero: ')))
numeros.append(float(input('Digite o 4º numero: ')))
numeros.append(float(input('Digite o 5º numero: ')))

print(max(numeros))
print(min(numeros))
soma = sum(numeros)
print(soma)
media = soma / len(numeros)
print(media)
