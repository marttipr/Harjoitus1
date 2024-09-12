# MONIKKO
###########

# Monikko (tuple) on kuin lita jota ei voi muokata

minun_lista = [1,2,3,4,5,6]
print(minun_lista)

minun_monikko = (1,2,3,4,5,6)
print(minun_monikko)

minun_monikko2 = (1,2,(3,4),5,'kuusi')
print(minun_monikko2)

# luetaan ensimmäinen alkio
print(minun_lista[0])
print(minun_monikko[0])

#yritetään nyt muokata eka alkio numeroiksi 0 ja lisätä loppuun 7
# listan sisältöä voi muokata, mutable
minun_lista[0] = 0
minun_lista.append(7)
print(f'muokattu lista {minun_lista}')
# monikon sisältöä EI voi muokata, immutable
#minun_monikko[0] = 0

# Monikkoa on tarkoituksenmukaista käyttää tilanteissa, joissa alkioiden jono on luonteeltaan staattinen
# tiedetään, että muutoksille ei ole tarvetta ohjelman suorituksen aikana
'''
# Koodiesimerkki materiaalista

viikonpäivät = ("maanantai", "tiistai", "keskiviikko", "torstai", "perjantai", "lauantai", "sunnuntai")
järjestysnumero = int(input('Anna viikonpäivän järjestysnumero (1-7):'))
viikonpäivät = viikonpäivät[järjestysnumero - 1]
print(f'{järjestysnumero}, viikonpäivä on {viikonpäivät}')
'''
# monikon läpikäynti kuten listan

# Monikon arvojen purku muuttujiin
sanalista = ('eka', 'toka', 'kolmas', 'neljäs', 'viides')

hedelmät = ('lime', 'sitruuna', 'Appelsiini')

#(eka, toka, kolmas) = ('lime', 'sitruuna', 'Appelsiini')
(eka,toka,kolmas) = hedelmät
print(eka)
print('----------------')

def tulosta_monikko(sanalista):
    for i in sanalista:
        print(i)

tulosta_monikko(sanalista)
tulosta_monikko(hedelmät)

# Monikko funktion paluuarvona

import random
def heitä2():

 eka, toka = random.randint(1,6), random.randint(1,6)
 return eka, toka

noppa1,noppa2 = heitä2()
print(f'Nopista tulee {noppa1}, {noppa2}')

# JOUKKO eli set{}

#joukko (set on järjestämätön tietorakenne, eli sen alkiot voivat olla missä tahansa järjestyksessä

#Koska joukon alkioille ei ole määritelty järjestystä, ei alkioihin voi myöskään viitata indeksillö

#toisin kuin listassa tai monikossa sama alkio voi esiintyä joukossa vain kerran, eli joukossa ei voi olla kahta samansisältöistä alkiota
joukko = {1,2,3,4,5,6}

print(joukko)

print(f' numero 6 voi esiintyä listassa useasti')
minun_lista = [6,2,3,4,5,6]
print(minun_lista)

print(f' numero 6 voi esiintyä listassa useasti')
minun_monikko = (6,2,3,4,5,6)
print(minun_monikko)

print(f' numero 6 EI voi esiintyä listassa useasti')
minun_joukko = {1,2,3,4,5,6}
print(minun_joukko)

#ylläoleva ei sinänsä tuora virhettä, kuten add - metodi

minun_joukko.add(6)
minun_joukko.add(7)
print(minun_joukko)
minun_joukko.remove(7)
print(minun_joukko)

pelit = {'Monopoli', 'Shakki', 'Cluedo'}
print (pelit)

pelit.add('Dominion')
print(pelit)

pelit.remove('Shakki')
print(pelit)
for p in pelit:
    print(p)
    #löytyykl Cluedo, jos läytyy printtaa jotaina
    if p == 'Cluedo':
        print('Cluedo löytyi')

if 'Monopoli' in pelit:
    print('Monopoli löytyi')


# tyhjä joukko luodaan edellä esitetystä poiketen set-funktiolla

autolista = []
autolista.append('Audi')
print(autolista)

autojoukko = {}
print(type(autojoukko)) # tämä on <class 'dict'>

autojoukko = set()
autojoukko.add('Audi')
print(type(autojoukko))  # tämä on <class 'set'>
print(autojoukko)

# SANAKIRJA

# Sanakirja (dictionary) on Pythonin kääytetyimipä tietorakenteita
# sanakirjaan voidaan tallentaa avain-arvopapereita

oppilaat = {'Aapeli': 25, 'Berti':19, 'Cecilia': 11,'Daniel' : 23, 'Emma' : 22}
print(oppilaat)

# mitä ovat tietueet eli items
print(oppilaat.items())

# mitä ovat avaimet sanakirjassa?
print(oppilaat.keys())

# mitä ovat arvoja sanakirjassa?
print(oppilaat.values())

# kun sanakirjaa käydään läpi for / in rakenteella:

# tietueet eli avain-arvoparit
for i in oppilaat:
    print(i)


#yksittäisen arvon haku avaimella
avain = 'Aapeli'
print(oppilaat[avain]) # etsii avaimella Aapeli sen arvoa joka on 25

# etsi kaikki arvot
for i in oppilaat:
    print(oppilaat[i])

# if / in rakenteella voidaan myös hakea sanakirjasta teitoa

nimi = input('Anna nimi, niin etsin sen sanakirjasta jos löytyy')
if nimi in oppilaat:
    print(f'Löytyi oppilas {nimi} ikä hänellä on {oppilaat[nimi]}')

# Lisätään uusi oppilas mikäli ei löydy
# jos avain löytyy, se muokkaaa olemassa olevaa, muuten luodaan uusi 
oppilaat['Bertta'] = 22
print(oppilaat)



nimet = ['Viivi', 'Ahmed']
numerot = ['050-1234567', '040-1112223']
print(f'{nimet}, numero: {numerot}')

yhteystiedot = {'Viivi': '050-1234567', 'Ahmed': '040-1112223'}
#print(f'Viivin numero: {yhteystiedot[Viivi]}')
hakusana = input('Puhelinnumerohaku, anna nimi:')
index = nimet.index(hakusana)
print(f'{hakusana}, numero: {numerot[index]}')
# sanakirjalla, hyödynnetään avainta
print(f'{hakusana}, numero: {yhteystiedot[hakusana]}')

#extra moniulotteinen sanakirja
yhteystiedot = {
    'Viivi': {'puh': '050-1234567', 'osoite': 'pikkutie 15'},
    'Ahmed': {'puh': '040-1112223', 'osoite': 'isotie 1'}

print(f'Viivin osoite {yhteystiedot["Ahmed"]["osoite"]}')
