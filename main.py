list1 = [1, 100, False, 10, 20]
del list1[2]

print(list1)

print(len(list1))

list1.sort(reverse=True)

print(list1)

list2 = ['abc', 3]

list3 = list1 + list2

list1.extend(list2)

print(list1)
print(list3)


list1.__add__(list2[:1])
print(list1)


