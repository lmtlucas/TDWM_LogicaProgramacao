preco=float(input('Digite o preço do produto: '))
desconto=preco*.95

if preco>=100:
    print(f'Total com desconto R${desconto}')
else:
    print(f'Total sem desconto R${preco}')