'''

take a input from user like . , ? / '
take another input from user and split it 3 on the basis of the previous input..

then print out the each splitted input
'''

splitter = input('Enter the string splitter')

a,b,c = input('Enter 3 strings seperated by ' + '\"' + splitter +'\"' + ' :').split(splitter)

print(a)
print(b)
print(c)
