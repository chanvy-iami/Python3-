# Python3条件控制
'''
Python条件语句是通过一条或多条语句的执行结果
来决定执行的代码块
'''

# if语句
'''
if condition1:
    block1
elif condition2:
    block2
else condition3:
    block3

'''

age = int(input('请输入你的年龄:'))  # 实例演示
if age <= 10:
    print('您是10后！')
elif (age > 10) & (age <= 20):
    print('您是00后!')
elif (age > 20) & (age <= 30):
    print('您是90后！')
else:
    print('您有点老！哈哈哈！')
input('Enter退出')

'''
# 操作符
<	小于
<=	小于或等于
>	大于
>=	大于或等于
==	等于，比较两个值是否相等
!=	不等于
'''

# if嵌套
'''
if 表达式1:
    语句
    if 表达式2:
        语句
    elif 表达式3:
        语句
    else:
        语句
elif:
    语句
else:
    语句
'''


