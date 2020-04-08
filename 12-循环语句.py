# while循环
'''
while 判断条件:
    语句
'''
n = 100
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1
print(sum)

# 无限循环
# var = 1
# while var == 1:
    # print('永远是请求')
'''
通过设置条件表达式永远不为false
无限循环在服务器上的客户端请求十分重要
'''

# while循环使用else语句
'''
在条件语句为false时执行else下的语句块
'''

# 简单语句组
'''
while循环体只有一条语句时，可写在一行上
'''

# for语句
'''
可遍历任何序列
'''
a = [123, 456, 'sni', [1, 2]]
for i in a:
    print(i)
b = 'vvfbvhfz'
for i in b:
    print(i)

# range()函数
for i in range(5):
    print(i)
for i in range(5, 9):
    print(i)
for i in range(0, 10, 2):
    print(i)                 # 可设置步长
c = ['ss', 'sff', 'dsvv', 'ssvss']
for i in range(0, len(c)):
    print(i, c[i])

# break和continue语句及循环中的else子句
'''
break语句直接终止循环
continue跳过当前循环的剩余语句，继续执行下一轮循环
'''

# pass语句
'''
空语句，保持程序结构完整性
'''