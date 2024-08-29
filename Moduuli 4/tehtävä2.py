while True:
    tuumat = float(input('anna tuumamäärä '))
    if tuumat <0:
        print('ohjelma lopetettu')
        break
    senttimetrit = tuumat * 2.54
    print(f'{tuumat} tuumaa on {senttimetrit: .2f}senttimetriä')
