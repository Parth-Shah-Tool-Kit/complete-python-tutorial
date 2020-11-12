'''
Input a name from the user
and then input argument to be searched
print the number of times the argument was present
'''

name = input("Enter your name: ")
arg = input("Enter query to be searched: ")

count = name.count(arg)

print(f"The query {arg} was present {str(count)} times")
