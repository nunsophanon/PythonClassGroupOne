input_list = [5,6,2,1,6,7,10,12]

def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False

for i in input_list:
    # print(i, "=>",i % 5)
    if div_by_five(i):
        print(i)

xyz = (i for i in input_list if div_by_five(i))
print(list(xyz))

# xyz = [i for i in input_list if div_by_five(i)]
# print(xyz)