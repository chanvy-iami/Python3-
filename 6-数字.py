# abs()函数

'''
abs()函数返回数字的绝对值
abs(x)
x为数值表达式，可以是整数、浮点数、复数
返回数字的绝对值，复数返回其大小
'''

print(abs(-5))
print(abs(3.63))
print(abs(complex(3, 4)))


# ceil()函数

'''
ceil()函数返回一个大于或等于x的最小整数
import math
math.ceil(x)
必须导入math模块，x为数值表达式
'''

import math
print(math.ceil(5.2))
print(math.ceil(-45.3))


# exp()函数

'''
exp(x)函数返回x的指数e^x
import math
math.exp(x)
x为数值表达式
'''

print(math.exp(2))


# fabs()函数

'''
fabs()函数类似abs()函数
abs()函数是内置函数，fabs()函数是math模块
fabs()函数只对浮点型和整数型数值有效
import math
math.fabs(x)
x是数值表达式
'''

print(math.fabs(-4))
print(math.fabs(4.5))


# floor()函数

'''
floor(x)函数返回数字的下舍整数，小于或等于x
import math
math.floor(x)
x为数值表达式
'''

print(math.floor(45.3))
print(math.floor(-45.3))


# log()函数

'''
log(x)函数返回x的自然对数，x>0
import math
math.log(x)
x为数值表达式
'''

print(math.log(100))


# log10()函数

'''
log10()函数返回以10位基数的x的对数，x>0
import math
math.log10()
x为数值表达式
'''

print(math.log10(10))


# max()函数和min()函数

'''
max()函数和min()函数分别返回参数的最大值和最小值
max(x, y, z, ...)
x, y, z为数值表达式
'''

print(max(50, 60, 30))
print(min(50, 60, 30))


# modf()函数

'''
modf(x)函数返回x的整数部分和小数部分，两部分的符号与x相同
import math
math.modf(x)
x为数值表达式
'''

print(math.modf(100.25))
print(type(math.modf(100.25)))


# pow()函数

'''
pow()函数返回x^y的值
import math
math.pow(x, y)
'''

print(math.pow(2, 2))


# round()函数

'''
round()函数返回浮点数的四舍五入值
round(x, n)
x为数字表达式，n为小数点位数
'''

print(round(100.63222, 1))


# sqrt()函数

'''
sqrt()函数返回数字的平方根
import math
math.sqrt(x)
x为数值表达式
'''

print(math.sqrt(25))


# choice()函数

'''
choice()函数返回一个列表、元组或者字符串中的随机项
import random
random.choice(seq)
seq为列表、元组或字符串
'''

import random
print(random.choice([1, 5, [1, 2], 'dsfs']))


# randrange()函数

'''
randrange()函数返回递增基数集合的一个随机数，基数默认为1
import random
random.randrange(start, stop, step)
start为开始值stop为结束值step为递增基数
返回指定范围的随机项
'''

print(random.randrange(1, 100, 2))


# random()函数

'''
random()函数返回随机生成的实数，范围[0,1)
import random
random.random()
无参数，返回随机实数
'''

print(random.random())


# seed()函数

'''
seed()函数改变随机数生成器的种子
import random
random.seed(x)
x为种子seed
无返回值
'''

random.seed()
print(random.random())


# shuffle()函数

'''
shuffle()函数将所有序列的所有元素随机排序
import random
random.shuffle(lst)
lst为列表
返回None
'''

lst = [1, 3, 6, 8, 9]
random.shuffle(lst)
print(lst)


# uniform()函数

'''
uniform()函数随机生成[x,y]范围内的下一个实数
import random
random.uniform(x, y)
x为随机数的最小值，y为随机数的最大值
返回浮点数
'''

print(random.uniform(2, 5))


# sin()、cos()、tan()函数

'''
import math
math.sin()
返回一个数值
'''

print(math.sin(3))
print(math.cos(3))
print(math.tan(3))


# asin()、acos()、atan()函数

'''
import math
math.asin()
返回反正弦值
'''

print(math.asin(1))
print(math.acos(1))
print(math.atan(1))


# atan2()函数

'''
atan2()返回给定xy坐标值的反正切值
import math
math.atan2(x, y)
xy为数值
'''

print(math.atan2(1, 2))


# hypot()函数

'''
hypot()函数返回欧几里德范数sqrt(x*x+y*y)
import math
math.hypot(x, y)
xy为数值
'''

print(math.hypot(3, 4))


# degrees()函数和radians()函数

'''
degrees()函数将弧度转换为角度
radians()函数将角度转换为弧度
import math
math.degrees(x)
x为数值
返回一个角度
'''

print(math.degrees(3))
print(math.radians(3))
