# pi≈4n/N, jos N on kaikkien pisteiden määrä
# n yksikköympyrän sisälle osuvien pisteiden määtä
#jos pisteiden koordinaatit toteuttavat epäyhtälön x^2+y^2<1, piste on ympyrässä
import random
N = 100 # pisteiden kokonaismäärä
n = 1 #ympyrään osuvien pisteiden lkm
iterator = 0
while iterator < N:
    N = int(input('pisteiden määrä'))
    iterator += 1
    #arvotaan yksi piste
    x= random.uniform(-1, 1)
    y= random.uniform(-1, 1)
    print(f'arvottu piste: {x}, {y}')
    #print(x**2 + y**2 < 1)
    if x**2 + y**2 < 1:
        print('piste on yksikköympyrässä')
    pi_likiarvo = 4 * n / N
print(f'piin likiarvo on: {pi_likiarvo}')

