'''
Take 3 user inputs
all there inputs should be in one input that are comma sperated...
then print the average of the three taken numbers
'''

a, b, c = input("Enter three coma seperated numbers").split(",")
print("average is: " + str(((float(a) + float(b) + float(c))/3)))
