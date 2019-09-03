import inspect

list1 = [1,2,3,4,5,6,7]


it = list1.__iter__()

print(it.__next__())
print(it.__next__())
print(it.__next__())
