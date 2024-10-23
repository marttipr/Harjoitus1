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

if __name__ == '__main__':
    autot = []
    for i in range(1,11):
        huippunopeus = random.randint(100, 200)
        rekisteritunnuts = f'ABC-{i}'
        autot.append(Auto(rekisteritunnuts, huippunopeus))
kilpailu_käynnissä = True
tunnit = 0
while kilpailu_käynnissä:
    tunnit += 1
    for auto in autot:
        nopeuden_muutos = random.randint(-10, 15)
        auto.kiihdyttää(nopeuden_muutos)
        auto.kulje(1)
        if auto.matka >= 10000:
            kilpailu_käynnissä = False


print(f" Kilpailu päättyi {tunnit} tunnin jälkee    n. Tulokset")
print(f"{'rekisteritunnus':<15} {'huippunopeus':<20} {'Tämänhetkinen nopeus (km/h)':30} {'Kuljettu matka (km):<20'}")
print("-" * 85)

for auto in autot:
    print(f'{auto.rekisteritunnus:<15} {auto.huippunopeus:<20} {auto.nopeus:<30} {auto.matka:<20.1f}')







