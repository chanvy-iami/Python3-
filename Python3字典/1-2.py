dict1 = {'Name': 'chen', 'Age': 28, 'Class': 3}

# copy()
dict2 = dict1.copy()   # 返回字典的浅复制
print(dict2)

# clear()
dict2.clear()          # 删除字典所有元素
print(dict2)

# fromkeys()
a = ('de', 'dt', 'dy')
print(type(a))
print(dict2.fromkeys(a))
print(dict2.fromkeys(a, 1))    # 创建新的字典，给定键，指定默认值

# get()
print(dict1.get('Name'))       # 返回指定键的值

# in操作符
print('Class' in dict1)
print('Name' not in dict1)     # 判断键是否存在字典

# items()
print(dict1.items())           # 遍历字典的键值，返回元组形式

# keys()
print(dict1.keys())            # 返回一个可迭代对象，键

# setdefault()
print(dict1.setdefault('Like', 'Basketball'))
# 类似get()函数，但如果不存在键值，则返回默认值

# update()
dict3 = {'qq': 1563}
dict1.update(dict3)
print(dict1)           # 将值更新到字典中

# values()
print(dict1.values())  # 返回可迭代对象，值

# pop()
print(dict1.pop('qq'))  # 删除键值对，并返回删除的值

# popitem()
dict1.popitem()         # 删除最后一个键值对
print(dict1)
