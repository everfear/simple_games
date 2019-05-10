# This is 'guess the number game'
import random

guessesTaken = 0

print('Hi! Tell me your name!')
myName = input()

number = random.randint(1, 20)
print('Well, ' + myName + ', i`m guessed the number from 1 to 20')

for guessesTaken in range(6):
    print('Try to guess it!')
    guess = input()
    guess = int(guess)

    if guess < number:
        print('Your number is too small!')

    if guess > number:
        print('Your number is too big!')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print('Great! ' + myName + ' you`ve done it in ' + guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Whoops, but i`ve guessed the ' + number + '.')

