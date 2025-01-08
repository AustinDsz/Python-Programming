# s1='K'
# print(s1, id(s1))

# s1 = "Hello"
# s2 = "World"

# print(s1, id(s1))
# print(s2, id(s2))


# print(s1[0])
# print(s1[-1])


# s1 = "Hello"
# print(s1, id(s1))
# s1 = s1.upper()
# print(s1, id(s1))



# String Interning
# Python will check character by character
# For each character python will create the object
# that object will be stored in the address
# then object and its address record will be stored in the string interning area
# this way python will save the memory by having similar character in one address

s1 = "Hello"
s2 = "World"

print(s1[2], id(s1[2]))
print(s2[3], id(s2[3]))