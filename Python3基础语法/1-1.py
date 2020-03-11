# 编码
'''
默认情况下，python3以UTF-8编码，所有字符串为unicode字符串
指定编码方式 # -*- coding: cp-1252 -*-
'''

# 标识符
'''
第一个字符必须是字母或者下划线
其他字符由字母、数字和下划线组成
标识符对大小写敏感
'''

# python保留字
import keyword
print(keyword.kwlist)
'''
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 
 'await', 'break', 'class', 'continue', 'def', 'del',
 'elif', 'else', 'except', 'finally', 'for', 'from', 
 'global', 'if', 'import', 'in', 'is', 'lambda', 
 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 
 'try', 'while', 'with', 'yield']
'''

# 注释
'''
单行注释：#
多行注释：多个#以及...
'''

# 行与缩进
'''
python特色，使用缩进来表示代码块
'''

# 多行语句
'''
total = item1 + \
        item2 + \
        item3
total = [],{},()不用使用\
'''

# 数字类型
'''
int;float;bool;complex
'''

# 字符串
'''
python中的单引号和双引号使用相同
三引号可以指定多行字符串
转义符"
反斜杠用来转义，r可以不发生转义
按字面意义级联字符串
+连接字符串 *重复字符串
python字符串索引方式，从左到右0开始，从右到左-1开始
python字符串不能改变
python无单独字符类型，一个字符就是长度为1的字符串
字符串截取的语法格式：变量[头下标:尾下标:步长]
'''
print('this is a book\nthis is a case')
print(r'this is a book\n this is a case')
print("this" "is" "book")
a = 'john'
b = 'mike'
print(a + b)
print(a * 2)
print(a[0:-1])
print(a[0:3:2])

# 空行
'''
分隔两段不同的代码
空行也是代码的一部分
'''

# 等待用户输入
# input("\n\n按下 enter 键后退出。")

# 同一行显示多条语句
'''
中间使用分号隔开
'''

# 多个语句构成代码组
'''
缩进相同的一组语句构成代码组
'''

# print输出
'''
print输出默认换行
如果不想换行，可在末尾加end=" "
'''
print('abcde')
print('ccvbg', end=" ")
print('fgjjg')
