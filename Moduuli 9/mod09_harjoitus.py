koirat = [
    {'Koira': 'Lissu', 'vuosi':2020},
    {'Koira': 'Reko', 'vuosi':2018}
]

#print(koirat)
#eka_koira = koirat[0]
#print(eka_koira['Koira'])


#--- Määritellään ensin luokka
# Luokka on 'ohje' olion luomiseen


class Koira:
   pass

# 2. Olio on luokan ilmentymä
#pääohjlemasta voi luoda useita olioita

# Lodaan koira-olio

ullan_koira = Koira()
aaron_koira = Koira()

#annetaan koira-olioile ominaisuuksia
# ominaisuudet ovat oliokohtaisia, kaikki ovat koiria mutta nimi, syntymävuosi, karvan laatu yms muuttuu


ullan_koira.nimi = 'Lissu'
ullan_koira.syntymavuosi = '2020'
aaron_koira.nimi = 'Reko'
aaron_koira.syntymavuosi = '2018'
aaron_koira.karva ='Lyhyt'

print(ullan_koira)
print(aaron_koira)
print(f'Ullan koiran nimi on {ullan_koira.nimi} ja syntymävuosi on {ullan_koira.syntymavuosi}')

#edellisessä esimerkissä tehtiin luokka ilman ominaisuuksia ja metodeja
#olion ominaisuudet annettiin yksi kerrallaan
#tämä on työlästäja oikea tapa onkin määritellä ja alustaa ominaisuudet luokan avulla


#Luokkien nimissä on CamelCase
class LuokanNimi:

# __init__ on funktio, erityinen sellainen, kutsutaan konstrukturiksi
# tätä funktiota kutsutaan aina auttomaattisesti kun luodaan luokasta olio / instanssi
# alustajan loppuun EI kirjoteta return lausetta
    def __init__(self, parametri1, parametri2):
        self.attribuutti1 = parametri1
        self.attribuutti2 = parametri2





'''

class Koira:

    def __init__(self, nimi, syntymavuosi, väri, koko):
        self.nimi = nimi
        self.syntymavuosi = syntymavuosi
        self.koko = koko
        self.väri = väri

    def printtaa_tiedot(self):
        print(f' Koiran nimi on {self.nimi} ja syntymävuosi on {self.syntymavuosi}')
        return

k1= Koira('Lissu', 2015, 'Musta', 'pieni')
k2=Koira('Reko', 2018, 'valkoinen', 'pieni')
k3=Koira('Mikki', 2019, 'keltainen,', 'Iso')
k4=Koira('Iiro', 2011, 'Oranssi', 'Pieni')
print(k4.nimi)

k1.printtaa_tiedot()

'''



class Koira:

    tehty = 0

    def __init__(self, nimi, syntymavuosi, väri, koko, haukahdus = 'HAUHAUHUAHUA'):
        self.nimi = nimi
        self.syntymavuosi = syntymavuosi
        self.väri = väri
        self.koko = koko
        self.haukahdus = haukahdus
        Koira.tehty = Koira.tehty + 1

    def printtaa_tiedot(self):
        print(f' Koiran nimi on {self.nimi} ja syntymävuosi on {self.syntymavuosi}')
        return

    def hauku(self, kerrat):
        print(f'{self.nimi} haukkuu {self.haukahdus} kertaa')
        for i in range(kerrat):
            print(self.haukahdus)
        return

k1 = Koira('Lissu', 2015, 'Musta', 'pieni', 'WOOF WOOOF')
k2 = Koira('Reko', 2018, 'valkoinen', 'pieni', 'Woooooof')
k3 = Koira('Mikki', 2019, 'keltainen,', 'Iso')
print(f'Koiria on yhteensä: {Koira.tehty}')
k2.hauku(3)