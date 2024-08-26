kuhan_pituus = float(input('mikä on kuhan pituus '))
puuttuu = 37 - kuhan_pituus
if kuhan_pituus < 37:
    print('laske kuha takaisin järveen'f' kuha on {puuttuu:.1f}cm liian lyhyt')
else:
    print('kuha on tarpeeksi pitkä')
