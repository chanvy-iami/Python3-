# int()函数

'''
int()函数用于将字符串或数字转换为整型
int(x, base=10)
x为字符串或数字，base为进制数，默认为十进制
返回整型数据
'''

print(int())
print(int(3.6))
print(int(12))
print(int('12', 16))
print(int('12', 8))  # 带base参数，x以字符串形式存在


# float()函数

'''
float()函数用于将整数和字符串转换成浮点数
float(x)
x为整数或字符串
返回浮点数
'''

print(float(1))
print(float('521'))


# complex()函数

'''
complex()函数用于创建一个值为real+imag*i的复数
或将字符串和数转换为复数，第一个参数为字符串，则不用指定第二个参数
返回一个复数
'''

print(complex(1, 2))
print(complex(1))
print(complex('1'))
print(complex(1+2j))  # 加号左右不能有空格


# str()函数

'''
str()函数将对象转换适合人阅读的形式
str(object='')
object对象
返回一个对象为string格式
'''

s = 'nowcoder'
print(str(s))
print(type(str(s)))


# repr()函数

'''
repr()函数将对象转化为供解释器读取的形式
repr(object)
object对象
返回一个对象为string格式
'''

s = 'nowcoder'
print(repr(s))
print(type(repr(s)))


# eval()函数

'''
eval()函数用来执行一个字符串表达式
eval(expression, globals, locals)
表达式，全局变量（字典对象），局部变量
返回表达式的结果
'''

a = 7
b = eval('3 * a')
print(b)


# tuple()函数

'''
tuple()函数将列表转换为元组
tuple(seq)
seq为转换成元组的序列
返回元组
'''

c = [1, 2, 'ash', [1, 2]]
d = tuple(c)
print(d)


# list()函数

'''
list()函数将元组或字符串转换为列表
list(seq)
seq为转换成列表的元组或字符串
返回列表
'''

str1 = 'i is jsi dddz'
list1 = list(str1)
print(list1)


# set()函数

'''
set()函数创建一个无需不重复元素集，可进行交并差集计算
set(iterable)
iterable为可迭代对象
返回新集合对象
'''

ss = set('acadc')
sss = set('cdacvb')
print(ss, sss)
print(ss & sss)
print(ss | sss)
print(sss - ss)


# dict()函数

'''
dict()用来创建一个字典
dict(**kwarg) dict(mapping, **kwarg) dict(iterable, **kwarg)
**kwarg 关键字 mapping 元素容器 iterable 可迭代对象
返回字典
'''

print(dict())
print(dict(a=1, b=2, c=3))  # 关键字
print(dict(zip(['a', 'b', 'c'], [1, 2, 3])))   # 映射函数方式
print(dict([('a', 1), ('b', 2), ('c', 3)]))    # 可迭代对象方式


# frozenset()函数

'''
frozenset()创建冻结的集合
frozenset(iterable)
iterable为可迭代对象，列表、字典、元组等
返回frozenset对象
'''

print(frozenset(range(10)))


# chr()函数

'''
chr()用一个范围在0~255的整数作参数，返回对应字符
chr(i)
i是十进制或十六进制的数
返回当前整数对应的ASCII字符
'''

print(chr(49))
print(chr(0x30))


# ord()函数

'''
chr()函数的配对函数
参数为字符
返回值为十进制数
'''

print(ord('a'))
print(ord('b'))


# hex()函数

'''
hex()函数将十进制整数转换为十六进制，以字符串形式表示
hex(x)
x为十进制整数
返回十六进制数，以字符串形式表示
'''

print(hex(12))
print(type(hex(12)))


# oct()函数

'''
oct()函数将一个整数转换成八进制字符串
oct(x)
x为整数
返回八进制字符串
'''

print(oct(10))


# id()函数

'''
id()函数用于获取对象的内存地址
id(object)
object对象
返回对象的内存地址
'''

di = 'dsnks'
print(id(di))
