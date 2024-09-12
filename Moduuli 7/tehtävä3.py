lentoasema = {}
def syötä_lentoasema():
    icao =input('Anna ICAO-koodi')
    nimi = input('Anna lentoaseman nimi')
    lentoasema[icao] = nimi
def hae_lentoasema():
 icao=input('Anna lentoaseman ICAO-koodi')
 if icao in lentoasema:
    print('Annettu lentoasema löytyy')
 else:
     print('Lentoasema ei löydy.')
while True:
    print('Valitse toiminto')
    print('1: syötä uusi lentoasema')
    print('2: hae lentoasema')
    print('3: exit')
    valinta = input('valintasi:')
    if valinta == '1':
        syötä_lentoasema()
    elif valinta == '2':
        hae_lentoasema()
    elif valinta == '3':
        print('ohjelma lopetetaan')
        break
    else:
        print('Virheellinen valinta, yritä uudelleen')

