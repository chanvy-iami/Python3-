list1 = [1, 2, 3, 4, 5]
tuple1 = (1, 2, 3)

# len()
print(len(list1))

# max()
print(max(list1))

# min()
print(min(list1))

# list()
print(list(tuple1))

# append()
list1.append(5)
print(list1)

# count()
print(list1.count(5))

# extend()
list1.extend([2, 3])
print(list1)

# index()
print(list1.index(1))

# insert()
list1.insert(5, 0)
print(list1)

# pop()
print(list1.pop())         # 默认为最后元素,并返回该值
print(list1)
list1.pop(5)        # 指定索引
print(list1)

# remove()
list1.remove(5)     # 移除第一个匹配项,无返回值
print(list1)

# reverse()
list1.reverse()
print(list1)

# sort()
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)

# copy()
print(list1.copy())

# clear()
list1.clear()
print(list1)
