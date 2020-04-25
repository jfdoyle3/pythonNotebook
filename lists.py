# Lists

# A list is enclosed by []
# A list can contain items of different types: [1, 'here', 2.3]
# lists works the same as in other languages
# mutable and dynamic
# lists methods works the same on Strings

stuff=[1,'whoopee',2.5,1000,'Careerdevs',3.333333]

# in works the same as lists bool true/false
print("Careedevs" in stuff ) # True

# get length of a lists
print(len(stuff)) # 6

# in  looks for char in lists: Boolean
print ('u' in stuff) # False
print ('z' in stuff) # False

# concatenation same as all other languages
# repeat the lists x number times
print(stuff[3]*5) # 5000

# b[0] returns D works like all other languages
# Using negtive index, starts at -1, will return end of lists
print (stuff[-1])  # 3.333333
print (stuff[-2])  # Careerdevs

# split into sub lists
print (stuff[1:3]) # ['whoopee', 2.5]
print(stuff[:])    # prints entire lists
print(stuff[:4])   # [1,'whoopee',2.5,1000]
print(stuff[:-4])  # [1, 'whoopee']
print ('--------------')
del stuff[2] # deletes/removes 'whoopee' from list

# List methods on numbered lists only. errors if mixed with Sttrngs
print(max(stuff)) # returns largest number in list
print(min(stuff)) # return smallest number in list
print(sum(stuff)) # adds all numbers in list
