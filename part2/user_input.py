'''

name = input("Write your name: ")
print("your name is: " + name)

number = input("Write a number: ")
print("the double of your number is: " + str(int(float(number) * 2)))

'''
'''
name, channel = 'Parth', 'TOOL KIT'

print(name + '\n' + channel)
'''

name, number = input('write your name and number: ').split(',')

print(name + '\n' + str(int(number)))
