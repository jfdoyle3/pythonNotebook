#Strings
# single quote or double quotes can be used
a='Single Quotes'
b="Double Quotes"
print( a,b)

# Triple single quote multi-line String with \n inserted
c='''This String is multi-lined
it inserts the \'\\n\' after
each return'''
print (c)

# get length of a string
print(len(c))

# in  looks for char in string: Boolean
print ('u' in c) # True
print ('z' in c) # False

# concatenation same as all other languages
# repeat the string x number times
print(a*5)

# b[0] returns D works like all other languages
# Using negtive index, starts at -1, will return end of String
print (b[-1]) # returns 's'
print (b[-2])  # returns 'e'

# split into sub Strings
print (c[1:3]) # prints the idx 1 - 3
print(c[:])    # prints entire String
print(c[:7])   # prints from idx 0 - 6
print(c[:-4])  # prints the string removes the last 4 chars


# String member methods
text="helllooo careerDevs   "

# Strips white spaces beginning and end of string
print(text.strip())

# Strips white spaces from beginning
print(text.lstrip())
# Strips white spaces from the end
print(text.rstrip())

# Changes to Upper and Lower case
print(text.upper())
print(text.lower())

print(text.isupper())        # bool
print(text.islower())        # bool
print(text.capitalize())     # capitalize the first char idx[0]
print(text.title())          #  title case 'hi there' to''Hi There'

print(text.startswith('H'))  # bool return: False
print(text.endswith('s'))    # bool return: False
print(text.replace('e','a')) # replaces all occurences

# Preferred: String format, one or more arguments accepted by using {}s
sentence='I am {} {} of the world'
print(sentence.format('on', 'top'))

# percentage place holders work too, works the same as other languages
words="Hey %s" # %s= string, %i = integer
print (words % "there")

numbers='1234'
print(numbers.ljust(5)) # left justifaction
print(numbers.rjust(5)) # Right justifaction
print(numbers.zfill(7)) # adds 0s to the beginning totaling the number
print(numbers.center(5)) # adds white space to 'center' text
