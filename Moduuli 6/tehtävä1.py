import random


def throw_dice():
    return random.randint(1,6)
result = 0
while result !=6:
    result = throw_dice()
    print(result)