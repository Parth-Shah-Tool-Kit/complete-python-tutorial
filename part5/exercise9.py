'''
take name input..
take age input..

if name begins with vowel
    print that you are lucky
if age is above 18
    print eligible for the ride
else
    if name begins with vowel
        lucky but not eligible
    else
        sorry not eligible
'''

name = input('Enter your name ')
age = int(input('Enter your age: '))

if name[:1] == 'A' or name[:1] == 'E' or name[:1] == 'I' or name[:1] == 'O' or name[:1] == 'U' or name[:1] == 'a' or name[:1] == 'e' or name[:1] == 'i' or name[:1] == 'o' or name[:1] == 'u': 
    print('You are lucky')

if age >= 18:
    print('eligible for the ride')
elif name[:1] == 'A' or name[:1] == 'E' or name[:1] == 'I' or name[:1] == 'O' or name[:1] == 'U' or name[:1] == 'a' or name[:1] == 'e' or name[:1] == 'i' or name[:1] == 'o' or name[:1] == 'u':
    print('lucky but not eligible')
else:
    print('sorry not eligible')
