#kirjota ohjelma, joka kysyy käyttäjältä kokonaisluvun ja kertoo onko se alkuluku


def is_prime_number(num):
    #jätetään nolla ja negatiiviset luvut kokonaan testaamatta
    if num <1:
        return False
    for i in range(2, num):
        print(i)
        if num % i == 0:
            #jos jaollinen jollain i:n arvolla, palautetaan false
            # ja funktion suoritus loppuu siihen
            return False
    #jos funktion suoritus on katkunut tänne asti paautetaan True
    return True
#pääohjelma lukeee syötteen ja tulostaa vastauksen
user_input = int(input('Anna testattava kokonaisluku (>0):'))
result = is_prime_number(user_input)
if result == True:
    print(f'luku {user_input} on alkuluku')
else:
    print(f'Luku {user_input} ei ole alkuluku')


# testataan funktion toimintaa erilaisilla arvoilla
#print(is_prime_number(4))
#print(is_prime_number(280))
#print(is_prime_number(0))
