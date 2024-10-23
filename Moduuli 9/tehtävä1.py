class Auto:
    def __init__(self,rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

if __name__ == '__main__':
    auto = Auto("ABC-123",142 )
    print(f'Rekisteritunnus on {auto.rekisteritunnus}')
    print(f'Auton huippunopeus on {auto.huippunopeus} km/h')
    print(f'Nopeus on {auto.nopeus} km/h')
    print(f'Kuljettu matka on {auto.matka} km')

