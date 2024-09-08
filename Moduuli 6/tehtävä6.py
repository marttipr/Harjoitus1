import math
def laske_yksikkohinta(halkaisija_cm, hinta_euroina):
    sade_cm = halkaisija_cm / 2
    pinta_ala_cm2 = math.pi * (sade_cm ** 2)
    pinta_ala_m2 = pinta_ala_cm2 * 1000
    yksikkohinta = hinta_euroina / pinta_ala_m2
    return yksikkohinta
def paohjelma ():
    halkaisija1 =float(input('Anna ensimmäisen pitsan halkaisja'))
    hinta1 = float(input('Anna ensimmäisen pitsan hinta'))
    halkaisija2 = float(input('Anna toisen pitsan halkaisija'))
    hinta2 = float(input('Anna toisen pitsan hinta'))
    yksikkohinta1 = laske_yksikkohinta(halkaisija1, hinta1)
    yksikkohinta2 = laske_yksikkohinta(halkaisija2, hinta2)
    print(f' Ensimmäisen pitsan yksikkohinta on {yksikkohinta1} per neliömetri')
    print(f'Toisen pitsan yksikkohinta on {yksikkohinta2} per neliömetri')
    if yksikkohinta1 < yksikkohinta2:
        print('ensimmäinen pizza tarjoaa paremman vastineen rahalle')
    elif yksikkohinta1 > yksikkohinta2:
         print('Toinen pizza tarjoaa paremman vastineen rahalle ')
    else:
         print('molemmat pizzat tarjoavat saman vastineen rahalle')
paohjelma()
