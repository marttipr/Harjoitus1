'''
name1 = 'Ville'
name2 = 'Nea'
name3 = 'Viola'
age1 = 6
age2 = 23
age3 = 17
print(f'Hei {name1} oletko {age1} vuotta vanha?')
print(f'Hei {name2} oletko {age2} vuotta vanha?')
print(f'Hei {name3} oletko {age3} vuotta vanha?')
print('-------------')

names = ['Ville', 'Nea', 'Viola', 'Kira','Juju','Ahmed', 'Lukas', 'Benjamin']
ages = [6, 23, 17,34,38,6]
print(f'{names}, {ages}')
length = len(names)
length2 = len(ages)
print(f' Listan pituus on {length}')
#alkiolla viitataan indeksinumerolla
names[0]
print(f'Hei {names[3]} ikäsi on {ages[3]} ')
print('---------')
#listan läpikäynti while. silmukan avulla
iterator = 0
while iterator < len(names):
    print(f'Hei {names[iterator]} ikäsi on {ages[iterator]} ')
    iterator += 1

    #names ['Ville', 'Nea', 'Viola', 'Kira','Juju']
lista = ['Ville', 'Nea', 'Viola', 'Kira','Juju','Ahmed', 'Lukas', 'Benjamin']
print(lista[1:5]) #2,3,4 (ei viimeistä
print(lista[2:]) #kaikki loput indeksin 2 alkaen
print(lista[-1]) #listan viimeinen alkio
print(lista[-1:-3:-1])
print(lista[2:6:2])
#listaan voi yhdistää ja siellä voi olla erilaisia tietorakenteita
lista1 = ['Karo', 'Jenna', 'Markus']
yhdistetty_lista = [18,35,75,60,55, lista1]
print(yhdistetty_lista)
print(yhdistetty_lista[5][0])
'''
lista = ['Ville', 'Nea', 'Viola', 'Kira','Juju','Ahmed', 'Lukas', 'Benjamin']
lista.append('Veikko')
if 'Juju'in lista:
    print('löytyy')
    lista.remove('Juju') #poistetaan alkio mikäli se löytyy, muuten virhe
lista.insert(0,'Juju')
lisaa_nimia = ['Aleksi','Vilho', 'Elias']
#lista.extend(lisaa_nimia)
#print(lista)

lista[1] = 'Neea'
print(lista)
lista.sort()
print(lista)
numero_lista = [1,5,3,6,7,4,12,4,56,]
numero_lista.sort()
print(numero_lista)
'''
for kirjain in 'abcde':
    print(kirjain)
for alkio in [1,2,3,4,5]:
    print(alkio)
for nimi in lista:
    print(nimi)
for numero in range(5,50,2):
    print(numero)
for i in range(999,0,-3):
    print(i)
'''
print(lista)
listan_pituus = len(lista)
for i in range(listan_pituus):
    print(f'Terve: {lista[i]}')
