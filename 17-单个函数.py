# Python format格式化函数

# 格式化字符串的函数
print('{} {}'.format('hello', 'world'))    # 默认对应
print('{0} {1}'.format('hello', 'world'))
print('{1} {0} {1}'.format('hello', 'world'))  # 按位置对应

# 通过参数对应
print('姓名:{name}, 年龄:{age}'.format(name='chenwei', age='25'))
a = {'name': 'chenwei', 'age': '25'}
print('姓名:{name}, 年龄:{age}'.format(**a))    # 通过字典设置参数
b = ['chenwei', '25']
print('姓名:{0[0]}, 年龄:{0[1]}'.format(b))     # 通过列表设置参数，其中0为必须的

# 数字格式化
print('{:.2f}'.format(3.1415926))    # 保留两位小数

print('{:+.2f}'.format(3.1415926))   # 保留符号

print('{:+.2f}'.format(-1))

print('{:.0f}'.format(2.2651))       # 去除小数位

print('{:,}'.format(1000000000))     # 以逗号分隔

print('{:.2%}'.format(0.25))         # 以百分比形式显示

print('{:.2e}'.format(100000000000))  # 以指数形式表示

print('{:#>10d}'.format(1355))       # 右对齐
print('{:#<10d}'.format(1355))       # 左对齐
print('{:#^10d}'.format(1355))       # 居中对齐

print('{:b}'.format(11))             # 二进制
print('{:d}'.format(11))             # 十进制
print('{:o}'.format(11))             # 八进制
print('{:x}'.format(11))             # 十六进制

print('{}对应位置为{{1}}'.format('nanncan'))   # {}可以进行转义

# input()函数
a = input('你的输入:')
print(type(a))
# 可接受任意性输入，默认字符串处理，并返回字符串

# 关于time的函数

# time.time()
import time
def procedure():
    time.sleep(2.5)
t0 = time.time()
procedure()
print(time.time() - t0)