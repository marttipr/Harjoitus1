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

if __name__ == '__main__':
    auto = Auto("ABC-123", 142)
    auto.kiihdyttää(30)
    auto.kiihdyttää(70)
    auto.kiihdyttää(50)

    print(f'Tämänhetkinen nopeus: {auto.nopeus} km/h')

    auto.kiihdyttää(-200)

    print(f'Nopeus jarrutuksen jälkeen on {auto.nopeus} km/h')
