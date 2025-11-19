compra=float(input('Informe o valor da compra: '))

if compra>=200:
    if compra>=500:
        print('Ganha frete grátis e brinde')
    else: 
        print('Frete grátis') 
else:
    if compra<=50:
        print('O valor do frete é R$ 20')
    else:
        print('O valor de frete é de R$ 10')