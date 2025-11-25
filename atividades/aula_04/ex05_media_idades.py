num_pessoas = 0
soma_idades = 0
idade = int(input("Digite a idade, ou 0 para finalizar: ")) 

if idade != 0:

    while idade != 0:
    
        num_pessoas += 1
        soma_idades += idade
        idade = int(input("Digite a idade, ou 0 para finalizar: ")) 

    media = soma_idades/num_pessoas
    print(media)   

else:
    print("nenhuma idade digitada")  