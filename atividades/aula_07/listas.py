# listas = []   
frutas = ['maçã', 'banana', 'uva']
numeros = [20, 10, 30, 55, 40]
vazia = []

print(frutas,numeros,vazia)

print(frutas[0]) # selecionando um item da lista pela posição

frutas[0] = 'abacate' # substituição do item 0
print(frutas)

# .sort modifica a lista ordenando-a
frutas.sort()
print(frutas)

# .sorted cria uma nova lista ordenando
frutas_ordenada_decrecente = sorted(frutas, reverse=True)
print(frutas_ordenada_decrecente)

numeros_ordenado = sorted(numeros)
print(numeros_ordenado)

# .append adiciona elemento no final da lista
frutas.append('morango')

print(frutas)

frutas.sort()
print(frutas)

# .extend adiciona varios elementos no final da fila aumentando o numero de indices de acordo com o numero de elementos inseridos
frutas.extend(['abacate', 'uvaia']) 
print(frutas)

# .insert adiciona elemento na posição desejada (posição, valor)
frutas.insert(0, 'manga') # posição 0
print(frutas)

# .remove remove um item da lista
frutas.remove('banana')
print(frutas)

# del remove uma posição especifica
del frutas[0]
print(frutas)

# max e min seleciona o maior ou o menor item da lista (para string considera ordem alfabetica)
maior_fruta = max(frutas) # criando nova variavel
print(maior_fruta)

# ou


print(min(numeros)) # modificando
