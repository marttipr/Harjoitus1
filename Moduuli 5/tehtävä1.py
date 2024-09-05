import random
total = 0
results = []
dice_count = int(input('monta noppaa laitetaan'))
for i in range(dice_count):
   total = total + random.randint(1,6)
   results.append(random.randint(1,6))
print(f'Noppien silmälukujen summa on {total}, nopat: {results}')
