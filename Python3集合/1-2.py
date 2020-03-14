set1 = {7, 8, 9, 2, 3}
set2 = {2, 3, 6, 9, 4}

# add()
set1.add(4)
print(set1)

# copy()
set3 = set1.copy()
print(set3)

# difference()
print(set1.difference(set2))    # 有返回值

# difference_update()
set1.difference_update(set2)    # 无返回值，改变原集合
print(set1)

# discard()
set1.discard(0)            # 元素不存在不会出错，但remove不同
print(set1)

# remove()
set1.remove(7)
print(set1)

# pop()
set1.pop()
print(set1)

# intersection()
print(set2.intersection(set3))

# intersection_update()
set2.intersection_update(set3)
print(set2)

# isdisjoint()
print(set2.isdisjoint(set3))    # 判断set2和set3中是否包含相同元素

# issubset()
print(set2.issubset(set3))      # 判断set2是否为set3的子集

# issuperset()
print(set2.issuperset(set3))    # 判断set2中是否全部包含set3的元素

# symmetric_difference()
print(set2.symmetric_difference(set3))    # 返回两个集合不重复的元素，即去除相同元素

# symmetric_difference_update()
set3.symmetric_difference_update(set2)    # 移除当前集合与另一个集合相同元素
print(set3)

# union()
print(set2.union(set3))   # 求并集，相同元素只出现一次

# update()
set1.update({1, 2})
print(set1)