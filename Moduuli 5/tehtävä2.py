numerot = []

luku = input('Anna luku tai syötä enter lopettaaksesi')
while luku != '':
    numerot.append(luku)
    luku = input('anna seuraava luku tai lopeta syöttämällä enter')
for num in numerot:
    print(f'{num}')
numerot.sort()
print(numerot)