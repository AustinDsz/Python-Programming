#if string is holding integer then it can be converted into int.

a='30'
print(a, type(a))
a=50
print(a, type(a))

#string to integer is not allowed
b='hello'
print(b, type(b))
# c=int(b)            # error
# print(c, type(c))

#float
# p = float(input("enter float type data \n"))
# print(str(p), type(p))

#bool

# q=12
# print(q, type(q))
# q=bool(q)
# print(q, type(q)) #prints True

q=''
q=bool(q)
print(q, type(q)) #false