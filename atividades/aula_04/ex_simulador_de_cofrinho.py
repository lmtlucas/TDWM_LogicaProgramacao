print('Simulador de cofrinho 1.0')

meta = float(input("Informe o valor que você quer juntar: R$ "))
total = 0
num_depositos = 0

while total < meta:
    deposito = float(input('Informe o deposito: R$ '))
    total += deposito # acumulador
    num_depositos = num_depositos + 1 # contador

print(f'Sua meta de R$ {meta:.2f} foi atingida\nVocê fez {num_depositos} depositos\nVocê juntou o total de R$ {total:.2f}')
