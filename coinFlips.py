import random


print('''I will flip the coin 1000 times. Guess how much "heads" appears? (Press Enter,
      to start flipping)''')
input()
flips = 0
heads = 0
while flips < 1000:
    if random.randint(0, 1) == 1:
        heads = heads + 1
        flips = flips + 1

        if flips == 900:
            print('900 flips and "Heads" appears ' + str(heads) + ' times.')
        if flips == 100:
            print('100 flips and "Heads" appears ' + str(heads) + ' times.')
        if flips == 500:
            print('Half of the road done, "Heads" appears ' + str(heads) + ' times.')

print()
print('From 1000 flips, "Heads" appears ' + str(heads) + ' times!')
print('How close you to the right answer?')
