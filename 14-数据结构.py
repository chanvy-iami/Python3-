# 列表

'''
列表可变，且存在多种方法
'''

# 将列表当作队列使用

# 列表推导式

'''
列表推导式提供从序列创建列表的途径
'''

a = [2, 3, 1]
b = [3*i for i in a]
print(b)

# 嵌套列表

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

trasmatrix = [[row[i] for row in matrix] for i in range(4)]
print(trasmatrix)

# del语句

'''
del语句通过列表索引来删除其中值
'''

# 元组和序列

# 集合

# 字典

# 遍历

