user_input = input('valitse LUX, A, B tai C ')
if user_input == 'LUX':
    print('LUX on parvekkeellinen hytti yläkannella.')
elif user_input == 'A':
    print('A on ikkunallinen hytti autokannen yläpuolella')
elif user_input == 'B':
    print('B on ikkunaton hytti autokannen yläpuolella')
elif user_input == 'C':
    print('C on ikkunaton hytti autokannen alapuolella')
else:
    print('Virheellinen hyttiluokka')
