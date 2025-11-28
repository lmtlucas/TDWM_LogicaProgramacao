num1 = int(input("Digite um numero par: "))

while num1 % 2 != 0:
    print("Este número não é par. Tente novamente.")
    num1 = int(input("Digite um numero par: "))
    if num1 % 2 == 0:
        break

num2 = int(input("Digite outro numero par: "))

while num2 % 2 != 0:
    print("Este número não é par. Tente novamente.")
    num2 = int(input("Digite outro numero par: "))
    if num2 % 2 == 0:
        break

print(f'Soma: {num1+num2}\nMédia: {(num1+num2)/2}')