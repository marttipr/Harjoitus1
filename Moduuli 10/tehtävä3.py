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

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissi_lkm):
       self.hissit = [Hissi(alin_kerros, ylin_kerros) for i in range(hissi_lkm)]
       self.hissien_lkm = hissi_lkm
       print(f'Talo luotu, jossa on {hissi_lkm} määrä hissejä.')
    def aja_hissiä(self,hissi_numero,kohde_kerros):
        if 1 <= hissi_numero <= self.hissien_lkm:
            print(f'Ajetaan hissiä {hissi_numero} kerrokseen {kohde_kerros}.')
            self.hissit[hissi_numero-1].siirry_kerrokseen(kohde_kerros)
        else:
            print('Hissin numero on väärä')
    def palohälytys(self):
        print('palohälytys! Hissit palaavat pohjakerrokseen')
        for i, hissi in enumerate(self.hissit, start=1):
            print(f'siirrytään {i} hissi pohjakerrokseen')
            hissi.siirry_kerrokseen(self.alin_kerros)

def main():
    talo= Talo(1,10,3)
    talo.aja_hissiä(1,10)
    talo.aja_hissiä(2,6)
    talo.aja_hissiä(3,3)
    talo.palohälytys()
if __name__ == '__main__':
    main()
