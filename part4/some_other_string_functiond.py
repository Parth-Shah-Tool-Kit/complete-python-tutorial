st = "He is a bad boy. She is a bad girl."
'''
my_name = "     Parth      Shah      "

print(my_name.lstrip())
print(my_name.rstrip())

print(my_name.lstrip().rstrip())

print(my_name.replace(' ',''))
'''

print(st.replace('crazy','good'))

in1 = st.find('is')
st2 = st[in1 + 1:]

print(st2.find('is') + len(st) - len(st2))
print(st[21])
