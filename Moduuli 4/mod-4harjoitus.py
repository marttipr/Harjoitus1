'''
#while-silmukat
# ikuinen silmukka, ei hyvä
while True:
    print('moro')
    print('matti')

max_count = int(input('how many times we greet'))
counter = 0
while counter < max_count:
    print(f'{counter}. kerran Hello')
    counter = counter + 1
print(f'laskurin arvo lopuksi: {counter-1}')
'''
# ohjelma komentorivikäyttöliittymä
import random
command = ''
while command != 'quit':
    command = input('Command, please>')
    if command == 'quit':
        print('lopetetaan.')
        #break #''heittää ulos'' silmukasta, ei paras ohjelmointikäytäntö
    elif command == 'Hello':
        max_count = int(input('how many times we greet'))
        counter = 0
        while counter < max_count:
            print(f'{counter}. Hello')
            counter = counter + 1
        print(f'laskurin arvo lopuksi: {counter}')
    elif command == 'noppa':
        rounds = 1000
        round_counter = 0
        total_rolls = 0
        while round_counter < rounds:
            round_counter += 1
            die1 = die2 = roll_counter = 0
            while die1 < 6 or die2 < 6:
                roll_counter += 1
                die1 = random.randint(1, 6)
                die2 = random.randint(1, 6)
                # print(f'{roll_counter}. heiton silmäluvut:{die1} ja {die2}')
            # print(f'noppaa heitettiin {roll_counter} kertaa')
            total_rolls = total_rolls + roll_counter
        print(f'Kaksi kutosta saatiin keskimäärin {total_rolls / rounds}')

    else:
        print('En ymmärrä komentoa. Yritä uudestaan, kiitos')
print('ohjelma sammutettu.')

'''
# noppapeli
# mikä on kahden yhtäaikaisen kutosen todennäköisyys
import random
rounds = 1000
round_counter = 0
total_rolls = 0
while round_counter < rounds:
    round_counter += 1
    die1 = die2 = roll_counter = 0
    while die1 < 6 or die2 < 6:
        roll_counter +=1
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        #print(f'{roll_counter}. heiton silmäluvut:{die1} ja {die2}')
    #print(f'noppaa heitettiin {roll_counter} kertaa')
    total_rolls= total_rolls + roll_counter
print(f'Kaksi kutosta saatiin keskimäärin {total_rolls/ rounds}')
'''