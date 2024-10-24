class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def siirry_kerrokseen(self,kohde_kerros):
        if kohde_kerros < self.alin_kerros or kohde_kerros > self.ylin_kerros:
            print('Virhe, kerros ei ole saatavilla!')

        while self.nykyinen_kerros < kohde_kerros:
            self.kerros_ylös()
        while self.nykyinen_kerros > kohde_kerros:
            self.kerros_alas()

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
            print(f'Hissi laskeutui! Nykyinen kerros:{self.nykyinen_kerros}')
        else:
            print('Hissi on alimmassa kerroksessa')

    def kerros_ylös(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
            print(f'Hissi nousi kerroksen! Nykyinen kerros:{self.nykyinen_kerros}')
        else:
            print('Hissi on ylimmässä kerroksessa')

def main():
    h = Hissi(1,10)
    h.siirry_kerrokseen(5)
    h.siirry_kerrokseen(1)
if __name__ == '__main__':
    main()

