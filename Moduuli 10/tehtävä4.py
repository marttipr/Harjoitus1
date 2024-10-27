import random


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
class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot
    def tunti_kuluu(self):
        for auto in self.autot:
            nopeuden_muutos = random.randint(-10,15)
            auto.kiihdyttää(nopeuden_muutos)
            auto.kulje(1)
    def tulosta_tilanne(self):
        print(
            f"{'Rekisteritunnus':<15} {'Huippunopeus (km/h)':<20} {'Tämänhetkinen nopeus (km/h)':<30} {'Kuljettu matka (km)':<20}")
        print("-" * 85)
        for auto in self.autot:
            print(f"{auto.rekisteritunnus:<15} {auto.huippunopeus:<20} {auto.nopeus:<30} {auto.matka:<20.1f}")
    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.matka >= self.pituus:
                return True
        return False

if __name__ == '__main__':
   autot = [Auto(f'ABC-{i}', random.randint(100,200))for i in range(1,11)]
   kilpailu = Kilpailu("Suuri romuralli", 8000, autot)
   tunnit = 0
   while not kilpailu.kilpailu_ohi():
       tunnit += 1
       kilpailu.tunti_kuluu()
       if tunnit % 10 == 0:
           print(f'Tunteja kulunut: {tunnit}')
           kilpailu.tulosta_tilanne()
print(f'Kilpailu päättyi {tunnit} tunnin jälkeen. Lopputilanne: ')
kilpailu.tulosta_tilanne()
