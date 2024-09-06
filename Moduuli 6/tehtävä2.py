import random


def throw_dice(overall):
    return random.randint(1,dice_max)
dice_max = int(input('Anna nopan suurin silmäluku'))
result = 0
while result == dice_max:
    result = throw_dice()
    print(result)
    