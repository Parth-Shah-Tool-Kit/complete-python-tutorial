'''
make a game

genrate a random number..
search on google how to genrate a random number...
take a input number

print whether it is equal less or greater than the number....
'''
import random

random_number = random.randint(0, 1)

inpu = input('enter a number...')

inpu = int(inpu)

if inpu < random_number:
    print('number is less')
elif inpu > random_number:
    print('number is bigger')
else:
    print('number is equal')

print('your number: '+ str(inpu) + '  random number: '+ str(random_number))
