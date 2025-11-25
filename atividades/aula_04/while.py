n=1

while n<10:
    print(n)
    n+=1

print(n)

senha_correta = 'python123'
tentativa = input('Digite a sua senha: ')

while tentativa != senha_correta:  #    != significa diferente
    print('Senha incorreta. Tente novamente')
    tentativa = input('Digite sua senha novamente: ')

print('Acesso liberado')

a=1

while a < 10:
    print(a)
    if a == 5:
        break
    a += 1

print(a)

num = input('Digite um numero ou 0 para sair: ')
