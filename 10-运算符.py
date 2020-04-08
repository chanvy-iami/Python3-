# 算术运算符

a, b = 2, 2.5
print(a + b)
print(b - a)
print(a * b)
print(b / a)
print(a % b)
print(a ** b)
print(b // a)

# 比较运算符

c, d = 5, 9
print(c == d)
print(c != d)
print(c > d)
print(c < d)
print(d >= c)
print(c <= d)

# 赋值运算符

e, f = 2, 6
g = e + f
print(g)
g += e
print(g)
g -= e
print(g)
g *= e
print(g)
g /= e
print(g)
g %= e
print(g)
g **= e
print(g)
g //= e
print(e)

# 位运算符
# 将数看成二进制来计算

h = 60
i = 13
j = h & i
print(j)
print(bin(j))
k = h | i
print(k)
print(bin(k))
m = h ^ i
print(m)
print(bin(m))
print(~h)
print(bin(h))
# 左移运算符
print(h << 2)    # 高位丢弃，低位补0
# 右移运算符
print(h >> 2)

# 逻辑运算符

p, q = 20, 30
print(p and q)
print(p or q)
print(not p)

# 成员运算符

list1 = [1, 3, 6, 8, 9]
print(1 in list1)
print(10 not in list1)

# 身份运算符
# 比较两个对象的存储单元

x, y = 20, 20
print(x is y)
print(x is not y)

# 运算符优先级

'''
**	指数 (最高优先级)
~ + -	按位翻转, 一元加号和减号 (最后两个的方法名为 +@ 和 -@)
* / % //	乘，除，取模和取整除
+ -	加法减法
>> <<	右移，左移运算符
&	位 'AND'
^ |	位运算符
<= < > >=	比较运算符
<> == !=	等于运算符
= %= /= //= -= += = *=	赋值运算符
is is not	身份运算符
in not in	成员运算符
not and or	逻辑运算符
'''


