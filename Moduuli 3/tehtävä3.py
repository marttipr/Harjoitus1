sukupuoli = (input('Anna sukupuoli'))
hemoglobiini = int(input('Anna hemoglobiiniarvosi'))
if sukupuoli == 'mies':
    if hemoglobiini < 134:
        print('hemoglobiini arvosi on liian alhainen')
    elif(134 <= hemoglobiini <= 195):
        print('hemoglobiini arvosi ovat tasiaset')
else:
    print('hemoglobiini arvosi ovat liian korkeat')
if sukupuoli == 'nainen':
    if hemoglobiini < 117:
        print('hemoglobiini arvosi on liian alhainen')
    elif(117 <= hemoglobiini <= 175):
        print('hemoglobiini arvosi ovat tasiaset')
    else:
     print('hemoglobiini arvosi ovat korkeat')
