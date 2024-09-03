kaupungit = []

nimi = input('Anna viiden kaupungin nimet')
while nimi != '':
    kaupungit.append(nimi)
    nimi = input('Anna viiden kaupungin nimet ja lopeta syöttämällä enter')
for nimi in kaupungit:
    print(f'{nimi}')