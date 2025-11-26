start = int(input('Insira o numero inicial para start: '))
stop = int(input('Insira o numero final para stop: '))
step = int(input('Insira o numero de intervalo para step: '))

for i in range(start, stop, step):
    print(i, end='  ')   # end= "" imprime em uma linha com o espaçamento que estiver entre ""