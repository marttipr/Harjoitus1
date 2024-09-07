import random


def throw_dice(overall):

    return random.randint(1,overall)

overall = int(input('Anna nopan suurin silmäluku'))
result = 0
while True:
    result =throw_dice(overall)
    print(f'Noppaa heitettiin: {result}')
    if result == overall:
        break
    