myfamily = ("mother", "father", "sister", "brother", "sister")

# 1. Use type()to check the type of the object myfamily
# <class 'tuple'>
print(type(myfamily))

# 2. Access tuple items sister by using index numbers
# We can print each element of tuple, also we can assign a value to a variable
print(myfamily[2])
sister = myfamily[2]

# 3. Check whether we can add an item me by using the append() method.
# "append()" is list method, we cannot use it to tuple, also tuple is unchangeable data type
# .but we can convert tuple to list and use "append()" method and then back to tuple
myfamily = list(myfamily)
myfamily.append("me")
myfamily = tuple(myfamily)
print(myfamily)

# 4. Check whether we can remove the item brother by using the pop() method.
# The "pop()" method removes the element at the specified position, in addition "pop()" is list method
# .but we can convert tuple to list and use "pop()" method and then back to tuple
myfamily = list(myfamily)
myfamily.pop(myfamily.index("brother"))
myfamily = tuple(myfamily)
print(myfamily)
