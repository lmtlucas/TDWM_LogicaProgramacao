nota1=float(input('Digite a nota da disciplina no 1ª bimestre: '))
nota2=float(input('Digite a nota da disciplina no 2º bimestre: '))
nota3=float(input('Digite a nota da disciplina no 3º bimestre: '))
nota4=float(input('Digite a nota da disciplina no 4º bimestre: '))
media=(nota1+nota2+nota3+nota4)/4

print(f'A média é: {media}')


if media>=6:
    print(f'Aprovado')
elif media>=5:
    print(f'Recuperação')
else:
    print('Reprovado')