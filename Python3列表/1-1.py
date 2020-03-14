'''
列表是python中最基本的数据结构
列表可索引、切片、加、乘、检查成员
列表内不需要具有相同类型的元素
'''
list1 = [1, 'sca', [1, 2]]
print(list1)

# 访问列表中的值
print(list1[0])       # 通过索引
print(list1[1:3])     # 通过切片

# 更新列表
list1[1] = 123        # 通过索引直接更新某个值
print(list1)

# 删除列表元素
del list1[2]
print(list1)

# 列表脚本操作符
print(len(list1))            # 长度
print(list1 + [1, 2, 6])     # 组合
print(list1 * 2)             # 重复
print(123 in list1)          # 判断元素是否存在
for i in list1:
    print(i)                 # 迭代输出

# 列表截取与拼接
print(list1[1])
print(list1[-1])
print(list1[0:1])

# 嵌套列表
list2 = [['a', 'b', 'c'], 1, 2, [5, 6, 9]]
print(list2[0][1])

# 列表函数与方法
# 函数
'''
len()               # 计算列表长度
max()               # 计算列表元素最大值
min()               # 计算列表元素最小值
list()              # 转换为列表
'''
# 方法
''' 
1   list.append(obj) 在列表末尾添加新的对象
2	list.count(obj) 统计某个元素在列表中出现的次数
3	list.extend(seq) 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
4	list.index(obj) 从列表中找出某个值第一个匹配项的索引位置
5	list.insert(index, obj) 将对象插入列表
6	list.pop([index=-1]) 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
7	list.remove(obj) 移除列表中某个值的第一个匹配项
8	list.reverse() 反向列表中元素
9	list.sort( key=None, reverse=False) 对原列表进行排序
10	list.clear() 清空列表
11	list.copy() 复制列表
'''