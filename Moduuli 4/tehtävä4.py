import random
oikea_luku = random.randint(1, 10)
while True:
    arvaus = int(input('arvaa luku 1-10'))
    if arvaus == oikea_luku:
        print('arvasit oikein')
        break
    if arvaus < oikea_luku:
        print('Liian pieni arvaus')
    if arvaus > oikea_luku:
        print('liian suuri arvaus')