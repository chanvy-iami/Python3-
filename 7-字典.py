'''
字典可以存储任意类型对象，可变容器
键值对组成
键必须是唯一的，但值不必是唯一的
'''

# 访问字典里的值
dict1 = {'Name': 'Mike', 'Age': 27, 'Area': 'Island'}
print(dict1['Name'])

# 修改字典
dict1['Age'] = 28         # 更新
dict1['Class'] = 1        # 添加新键值对
print(dict1)

# 删除字典元素
del dict1['Class']        # 删除字典的键
print(dict1)
# dict1.clear()            # 清空字典
# print(dict1)
# del dict1                 # 删除字典，即未定义

# 字典键的特性
'''
1.不允许同一个键出现两次，如果同一个键赋值两次，后一个被记住
2.键必须是不可变的，可以是字符串、元组、数字，但列表不可以
'''

# 字典内置函数和方法
# 内置函数
print(len(dict1))        # 计算字典元素个数，即键的总数
str(dict1)               # 输出字典，以可打印的字符串表示
print(type(dict1))       # 输出类型

# 方法
'''
1	radiansdict.clear() 删除字典内所有元素
2	radiansdict.copy() 返回一个字典的浅复制
3	radiansdict.fromkeys() 创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
4	radiansdict.get(key, default=None) 返回指定键的值，如果值不在字典中返回default值
5	key in dict 如果键在字典dict里返回true，否则返回false
6	radiansdict.items() 以列表返回可遍历的(键, 值) 元组数组
7	radiansdict.keys() 返回一个迭代器，可以使用 list() 来转换为列表
8	radiansdict.setdefault(key, default=None) 和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
9	radiansdict.update(dict2) 把字典dict2的键/值对更新到dict里
10	radiansdict.values() 返回一个迭代器，可以使用 list() 来转换为列表
11	pop(key[,default]) 删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
12	popitem() 随机返回并删除字典中的最后一对键和值。
'''

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
