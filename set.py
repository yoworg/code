import inspect

list1 = [1,2,3,4,5]


it = list1.__iter__()

print(it.__next__())
print(it.__next__())
print(it.__next__())
