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

# luodaan osoitin ja sijoitetaan muuttujaan
cursor = connection.cursor()
# ajetaan SQL-kielinen kysely  osoittimen avulla
cursor.execute('select continent, name, iso_country from country')
#fetchone hakee rivi kerrallaan, palauttaa monikon
result = cursor.fetchone()
#fetchmany() palauttaa halutun määrän rivejä (monikko kerrallaan listana
result = cursor.fetchmany(3)
#print(result)
# fetchall () palauttaa kaikki (loput) rivit listana
rows = cursor.fetchall()
print(rows)
#tuloslista käsitellään toistorakenteella
for row in rows:
    print(f'{row[1]}: Maakoodi: {row[2]}, maanosa: {row[0]}')