'''
alustus ehtolauseelle

rahat = float(input('Anna rahamääräsi:'))

if rahat >= 5:
    print('voit ostaa latten, sinulla on tarpeeksi raha')

print( 'jatketaan pääohjelmaa')


 sama kuin:
 rahat=float(input('anna rahamääräsi'))
 ehto = (rahat >=5)
 print(ehto)
 if ehto:
 print('voit ostaa latten, sinulla on tarpeeksi raha')
print( 'jatketaan pääohjelmaa')
suutari = input ('anna suutarin nimi')
raatali = input ('anna raatalin nimi')
if suutari == raatali:
    print('Hyvänen aika! Suutari ja raatali ovat kaimoja')


luku = int(input('Anna luku: '))
if luku > 0:
    print('luku on positiivinen')
if luku < 0:
    print('luku on negatiivinen')
if luku == 0:
    print('luku on nolla')

# kaksi toisensa poissulkevaa vaihtoehtoa
rahat = float(input('Anna rahamäärä:'))
if rahat >= 5:
    print('voit ostaa latten.')
else:
    print('sinulla ei ole tarpeeksi rahaa')
# monta vaihtoehtoa

user_input = input('valitse a,b,c:')
if user_input == 'a':
    print('Tehdään jotain, käyttäjä valitsi kirjaimen a')
elif user_input == 'b':
    print('tehdään muuta kiva, käyttäjä valitsi b')
elif user_input == 'c':
    print('käyttäjä valitsi c')
else:
    print('Käyttäjä ei syöttänyt a,b tai c. ei tehdä mitään')

print('ohjelma loppuu, hei hei')

age = 5
name = 'matti'

print(age < 10 and name == 'matti') #ture

# True False
print(age < 10 and name == 'kari') # false

# or
print(age <10 or name == 'kari')

print(True and True)
print(False and True)
print(True or True)
print(False or True)
print(True and(False or True))

result = (False or False) and (False or True)
print(f'vertailun tulos: {result}')
print(1 < 2 or (1 == 1 and result == True))

# while-silmukat
# ikuinen silmukka, ei hyvä
while True:
    print('moro')
    print('matti')
'''

counter = 0
while counter < 5:
    print(f'{counter}. kerran Hello')
    counter = counter + 1
print(f'laskurin arvo lopuksi: {counter-1}')