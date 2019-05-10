import random
import time


def displayIntro():
    print('''You are in dragonland!
You see two caves in fron of you. One cave with good dragon,
which will give you some of their treasure. Second cave with evil dragon,
he will eats you as fast as you will step in his cave!.''')
    print()


def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you choose? (Press key 1 or key 2)')
        cave = input()

    return cave


def checkCave(chosenCave):
    print('You are coming close to cave...')
    time.sleep(2)
    print('Cave looks dark and creepy, you scared...')
    time.sleep(2)
    print('Big dragon jumps in front of you! He opens his mouth and...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('...give you bag of gold!')
    else:
        print('...eats you!')


playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print('Will you try your luck again? (yes or no)')
    playAgain = input()
