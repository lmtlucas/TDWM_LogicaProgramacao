frutas = []
frutas.insert(int(input('digite a posição: ')), input('Digite a fruta: '))
add = input('Quer adicionar outra fruta ou ver lista completa? (Digite adicionar/lista) : ')

while add=='adicionar':
        frutas.insert(int(input('digite a posição: ')), input('Digite a fruta: '))
        add = input('Quer adicionar outra fruta ou ver lista completa? (Digite adicionar/lista) : ')


print(frutas)