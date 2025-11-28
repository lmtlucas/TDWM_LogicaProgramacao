valor_produto = float(input("Digite o valor do produto (ou digite 0 para parar): R$ "))
total = 0
num_produtos = 0

while valor_produto != 0:
    total += valor_produto # acumulador
    valor_produto = float(input("Digite o valor do produto (ou digite 0 para parar): R$ "))
    num_produtos = num_produtos + 1 # contador

print(f'Quantidade de itens da compra: {num_produtos}\nValor final: R${total}')

if total > 200:
    print("Valor pode ser parcelado em até 3 vezes")
elif total > 100:
    print("Valor pode ser parcelado em até 2 vezes")
elif total > 50:
    print("Valor pode ser pago via cartão de crédito em 1 vez")
else:
    print("Valor pode ser pago somente via débito ou pix")

