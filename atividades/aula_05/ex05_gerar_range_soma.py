start = int(input('Insira o numero para start: '))
stop = int(input('Insira o numero para stop: '))
step = int(input('Insira o numero para step: '))

total = 0

for i in range(start, stop, step):

    print(i, end='  ')  
    total+=i

print(f'\nA soma é: {total}')