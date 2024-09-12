def anna_vuodenaika(kuukausi_numero):
    vuodenaika_dict = {
        'Kevät': [3,4,5],
        'Kesä':[6,7,8],
        'Syksy':[9,10,11],
        'Talvi':[12,1,2]
    }
    for vuodenaika, kuukaudet in vuodenaika_dict.items():
        if kuukausi_numero in kuukaudet:
            return vuodenaika
    else:
        print('Virheellinen kuukausinumero')

kuukausi_numero =int(input('Anna kuukausi numerona (1-12):'))
vuodenaika = anna_vuodenaika(kuukausi_numero)
print(f'Vuodenaika on {vuodenaika}')
