a = int(input('enter a number'))
'''
if a > 100:
    if a % 2 == 0:
        if a % 3 == 0:
            print('Condition satisfied')
        else:
            print('%2, >100 but not %3')
    else:
        if a % 3 == 0:
            print('>100, not %2 but %3')
        else:
            print('>100 but not %3,%2')
else:
    if a % 2 == 0:
        if a % 3 == 0:
            print('<100 and satisfied')
        else:
            print('%2, <100 but not %3')
    else:
        if a % 3 == 0:
            print('<100, not %2 but %3')
        else:
            print('<100 but not %3,%2')
'''
if a > 100 and a % 2 == 0 and a % 3 == 0:
    print('Condition satisfied')
else:
    print('not satisfied')
