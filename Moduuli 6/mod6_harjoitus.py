'''
def do_something():
     print('Doing')
     print('Something')
     return 'tässä on palautettava arvo, voi olla ihan minkä tyyppinen vaan'

return_value = do_something()
print(return_value)
#funktio jolla parametreja (argumentteja)
def combine_strings(word1, word2):
    combination = f'{word1}, {word2}'
    print(combination)

combination = combine_strings('auto', 'ajaa')
combination = combine_strings('kuski', 'ajaa')
print(combination)

from pkg_resources import non_empty_lines


#yksinkerainen laskin, jolle voi antaa vain tasan kaksi paramteria

def calculate(calc_type, number1, number2):
   if calc_type == 'sum':
       return number1 + number2
   elif type == 'division':
       return number1 / number2
   #return None

print(calculate('sum', 2.4,3.5))
print(calculate('division', 2.4,3))

import numbers


def calculate_sum(numbers):
    total_sum = 0
    for num in numbers:
        total_sum = total_sum + num
    return total_sum

nums = [3,4,5]
print(calculate_sum(nums))
print(calculate_sum([2,3,8,-10,4.67]))
print('----------')


def calculate2(number1, number2, calc_type='sum'):
    if calc_type == 'sum':
        return number1 + number2
    elif type == 'division':
        return number2 / number1
    print(calculate2(2.4,3.5))
    print(calculate2(number2=2.4, number1=3.5,calc_type='division'))
'''

