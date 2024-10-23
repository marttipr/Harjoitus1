class Auto:
    def __init__(self,rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdyttää(self, nopeuden_muutos):
        uusi_nopeus = self.nopeus + nopeuden_muutos

        if uusi_nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.nopeus = 0
        else:
            self.nopeus = uusi_nopeus

    def kulje(self, tuntimäärä):
        self.matka += self.nopeus * tuntimäärä

if __name__ == '__main__':
    auto = Auto("ABC-123", 142)

    auto.kiihdyttää(80)
    auto.matka = 3000
    auto.kulje(2)

    print(f' Tämänhetkinen nopeus on {auto.nopeus} km/h')
    print(f' Kuljettu matka: {auto.matka} km')
