# this is a commented line
# semicolons can be used, but it;s not practised.
print('Resistence is futile!')
print(3**4)

# semicolon can be used to compound statements
print('This string and math are on a single line'); print(2**4)

# Intergers can be declared in one line
a,b,c,d=1,2,3,4
print (a,b,c,d)

e=f=g=h=7
print(e,f,g,h)

# delete a declared varible
del h
# print (h) will cause an error:

# using a deleted variable returns an error:
# Traceback (most recent call last):
#   File ".\simpleStatements.py", line 18, in <module>
#     print (h)
# NameError: name 'h' is not defined
