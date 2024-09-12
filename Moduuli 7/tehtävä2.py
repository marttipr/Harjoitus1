nimet = set()
while True:
    nimi =input('Anna nimi(tyhjä lopettaa)')
    if nimi == '':
        break
    if nimi in nimet:
        print('Aiemmin syötetty')
    elif nimi not in nimet:
        print('Uusi nimi')
        nimet.add(nimi)
print("Syötetyt nimet")
for nimi in nimet:
    print(nimi)
