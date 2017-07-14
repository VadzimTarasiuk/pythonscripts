list1 = [0, 'somename', 24]
length1 = len(list1)
list2 = ['index', 'name', 'age']
length2 = len(list2)
somedict = {}
if length1 < length2:
    for i in range(length2):
        if i < length1:
            somedict[list2[i]] = list1[i]
        else:
            somedict[list2[i]] = None
else:
    for i in range(length2):
        somedict[list2[i]] = list1[i]
print(somedict)