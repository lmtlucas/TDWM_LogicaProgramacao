lista = []
item = input('Digite o item da lista de compras (ou 0 para parar): ')


while item != '0':
    lista.append(item)
    item = input('Digite o item da lista de compras (ou 0 para parar): ')



print(lista)