x = [1,2,3,4,8,6]
y = [7,8,3,2]
z = ['a','b','c','d','e']

#The zip function iterates through multiple iterables, and aggregates them.

#zip x and y together
# for a,b in zip(x,y):
#     print(a,b)

#zip x, y and z together
for x,y,z in zip(x,y,z):
    print(x,y,z)

# print(list(zip(x,y,z)))
print(x)


# [print(x,y,z) for x,y,z in zip(x,y,z)]
