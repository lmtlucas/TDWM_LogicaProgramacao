passou_de_ano=input('Você passou de ano? (sim/não)').strip().lower()
passou_no_vestibular=input('Você passou no vestibular? (sim/não):').strip().lower()

if passou_de_ano=='sim':
    if passou_no_vestibular=="sim":
        print('começará a faculdade no próximo ano.')
    else:
        print('tente o vestibular novamente')
else:
    print('precisa estudar mais para passar de ano')