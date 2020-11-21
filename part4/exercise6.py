'''

input a string
print 1,2,3 position of argument entered by the user
'''

st = input("Enter: ")
arg = input("arg: ")

i1 = st.find(arg)
i2 = st[i1 + 1:].find(arg)
i3 = st[i2 + 1:].find(arg)

print(i1)
print(i2)
print(i3)
