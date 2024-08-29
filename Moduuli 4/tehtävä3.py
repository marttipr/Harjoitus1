max_num = min_num = int(input('syötä luku'))
while True:
    input_string = input('syötä luku:')
    if input_string == '':
        break
    number = int(input_string)
    if number > max_num:
        max_num = number
    if number < min_num:
        min_num = number
print(f'pienin numero:{min_num} , suurin numero:{max_num}')
