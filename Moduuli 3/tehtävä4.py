vuosi = int(input('anna vuosi'))
if vuosi % 4 == 0 and vuosi % 100 != 0 and vuosi % 400 == 0:
    print('vuosi on karkausvuosi')
else:
    print('vuosi ei ole karkausvuosi')
