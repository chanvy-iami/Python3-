'''
集合是无序无重复的序列
创建集合{}，set（），空集合时必须是set（)
'''

# 添加元素
set1 = {1, 2, 5}
set1.add(1)
print(set1)           # 元素已经存在，不执行任何操作
set1.update({3, 6})   # 添加多个元素
print(set1)

# 移除元素
set1.remove(2)
print(set1)         # 元素不存在，发生错误
set1.discard(2)
print(set1)         # 元素不存在，不发生错误
set1.pop()
print(set1)         # 随机删除，默认为排序后的第一个

# 计算集合元素个数
print(len(set1))

# 清空集合
set1.clear()
print(set1)

# 判断元素是否在集合中
set2 = {2, 5, 6, 9, 8}
print(2 in set2)

'''
add()	为集合添加元素
clear()	移除集合中的所有元素
copy()	拷贝一个集合
difference()	返回多个集合的差集
difference_update()	移除集合中的元素，该元素在指定的集合也存在
discard()	删除集合中指定的元素
intersection()	返回集合的交集
intersection_update()	返回集合的交集
isdisjoint()	判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。
issubset()	判断指定集合是否为该方法参数集合的子集
issuperset()	判断该方法的参数集合是否为指定集合的子集
pop()	随机移除元素
remove()	移除指定元素
symmetric_difference()	返回两个集合中不重复的元素集合
symmetric_difference_update()	移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。
union()	返回两个集合的并集
update()	给集合添加元素
'''

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

