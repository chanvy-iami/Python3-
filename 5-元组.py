'''
python元组与列表相似，但元组的元素不能改变
元组为圆括号，列表是方括号
创建空元组tuple = ()
只有一个元素时，tuple = (1,)，不加逗号认为是运算符
'''

# 访问元组
tuple1 = (1, 5, 6, 'hji')
print(tuple1[2])           # 通过索引

# 修改元组
# tuple1[0] = 0           # 非法
tuple2 = (4, 6, 9)
print(tuple1 + tuple2)

# 删除元组
del tuple2
# print(tuple2)         # 元组元素不能删除，删除整个元组有异常

# 元组运算符
a1 = (1, 2, 3)
a2 = (4, 5, 6)
print(a1 + a2)
print(a1 * 2)

# 元组索引，截取
print(a1[0])
print(a1[0:2])

# 元组内置函数
print(len(a1))
print(max(a1))
print(min(a1))
a3 = [1, 6, 8]
a4 = tuple(a3)
print(type(a3))
print(type(a4))
print(a4)