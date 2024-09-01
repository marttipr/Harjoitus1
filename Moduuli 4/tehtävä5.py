oikea_kayttajatunnus = 'python'
oikea_salasana = 'rules'

yritykset = 0
max_yritykset = 5

while yritykset < max_yritykset:
    kayttajatunnus = input('anna käyttäjätunnus')
    salasana=input('anna salasana')

    if kayttajatunnus == oikea_kayttajatunnus and salasana == oikea_salasana:
        print('tervetuloa')
        break
    else:
        print('väärä käyttäjätunnus tai salasana')
        yritykset+=1
if yritykset == max_yritykset:
    print('pääsy estetty')