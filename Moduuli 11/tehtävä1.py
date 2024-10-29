class Julkaisu:
    def __init__(self, nimi,vuosi):
        self.nimi = nimi
        self.julkaisuvuosi = vuosi


    def tulosta_tiedot(self):
        print(f'Julkaisun nimi:{self.nimi} ja julkaisuvuosi {self.julkaisuvuosi}')



class Kirja(Julkaisu):
    def __init__(self,nimi,julkaisuvuosi, kirjailia, sivumäärä):
        super().__init__(nimi, julkaisuvuosi)
        self.kirjailia = kirjailia
        self.sivumäärä = sivumäärä
    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f'Kirjan kirjailia:{self.kirjailia} ja sivumäärä on {self.sivumäärä}')

class Lehti(Julkaisu):
    def __init__(self,nimi,julkaisuvuosi, päätoimittaja):
        super().__init__(nimi, julkaisuvuosi)
        self.päätoimittaja = päätoimittaja

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f'Lehden päätoimittaja on {self.päätoimittaja}')




j = Julkaisu('Magea Magaziini', 2015)
#print(j.nimi)

k = Kirja("Hytti n:o 6", 2014,"Rosa Liksom", 200)
#print('Kirjan nimi', k.nimi)

l = Lehti("Aku Ankka", 1994,"Aki Hyyppä")
#print('Päätoimittaja', l.päätoimittaja)

k.tulosta_tiedot()
print('-----------------')
l.tulosta_tiedot()