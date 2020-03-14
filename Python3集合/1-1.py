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

