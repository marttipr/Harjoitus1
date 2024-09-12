import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='pruulmartti',
         password='salakala',
         autocommit=True,
         collation='utf8mb4_general_ci',
 )



def fetch_airport_by_icao(code):
    sql = (f"SELECT  name, municipality "
           f" FROM airport WHERE ident= '{code}'")
   # print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result_row = cursor.fetchone()
    return  result_row

user_input = input('Syötä ICAO-koodi:')
airport = fetch_airport_by_icao(user_input)


if airport: #vastaava: airport != None
    print(f'Haettu lentokenttä: {airport[0]}, {airport[1]}.')
else:
    print('Lentokenttää ei löydetty annetulla koodilla')

#EXTRA tiedon lisäys
def add_airport(icao, name, municipality):
    sql = (f"Insert INTO airport(id, idnet, name, municipality)"
           f"VALUES (999, '{icao}', '{name}', '{municipality}'");
    cursor = connection.cursor()
    cursor.execute(sql)
icao = input('Anna uusi ICAO:')
name = input('Anna uusi kentän nimi:')
municipality = input('JA paikkakunta:')
add_airport(icao, name, municipality)



