str1 = 'Hello World'
str2 = 'I am Jho'

# Python访问字符串中的值
print(str1[0])
print(str2[1:3])

# Python字符串更新
print(str1 + str2[4:8])

# Python转义字符

# Python字符串运算符
print(str1 + str2)      # 字符串连接
print(str1 * 2)         # 输出重复字符串
print(str1[2])          # 索引字符串
print(str1[0:5])        # 截取字符串
print('H' in str1)
print('J' not in str1)  # 判断字符是否在字符串中
print('jjjdjs\nkskk')
print(r'jjjdjs\nkskk')  # 输出原始字符串

# Python字符串格式化
print('我叫%s,今年%d岁。' % ('小明', 25))

# Python三引号

# Unicode字符串

# Python的字符串内建函数

str1 = 'i like Basketball!'

# capitalize()
print(str1.capitalize())     # 首字母大写

# center()
print(str1.center(30, '*'))  # 居中对齐，默认空格填充

# count()
print(str1.count('i', 0, len(str1)))  # 计算子字符的个数，可定义起始位置和结束位置

# endswith
print(str1.endswith('l', 0, len(str1)))    # 判断字符串在指定范围内是否以某个字符结尾

# startswith()
print(str1.startswith('i', 0, len(str1)))   # 判断字符串在指定范围内是否以某个字符开头

# expandtabs()
str2 = 'you\tare fool'
print(str2.expandtabs())
print(str2.expandtabs(16))          # 将字符串中的\t替换，默认8个字符，可指定替换字符数

# find()
print(str1.find('a'))      # 返回第一个匹配的字符索引

# rfind()
print(str1.rfind('i'))         # 返回某个字符最后的索引，无返回-1

# index()
print(str1.index('i'))     # 返回第一个匹配的索引值

# isalnum()
print(str1.isalnum())      # 字符是否由字母和数字组成

# isdigit()
print(str1.isdigit())
str3 = '123456'
print(str3.isdigit())      # 字符是否由数字组成

# isdecimal()
print(str1.isdecimal())     # 判断字符串中是否只包含十进制字符
str12 = '566'
print(str12.isdecimal())

# isalpha()
print(str1.isalpha())      # 字符是否全部由字母组成

# islower()
print(str1.islower())      # 字符是否全部小写

# isnumeric()
# 判断字符串是否只由数字组成，数字包括全角、半角、罗马、汉字数字等

# isspace()
print(str1.isspace())      # 字符只由空白字符组成

# istitle()
print(str1.istitle())       # 判断字符中的每个字母是否大写

# isupper()
print(str1.isupper())       # 字符是否全部大写

# join()
str4 = '-'
print(str4.join(str1))      # 以指定字符连接某个字符串

# len()
print(len(str1))            # 计算字符串的字符长度

# ljust()
print(str1.ljust(30, '*'))   # 左对齐

# rjust()
print(str1.rjust(30, '*'))   # 右对齐

# lower()
print(str1.lower())          # 全部转换为小写

# upper()
print(str1.upper())           # 全部转换为大写

# lstrip()
print(str1.lstrip('i'))       # 截掉字符串左边指定字符，默认空格

# rstrip()
print(str1.rstrip('!'))       # 截掉字符串右边指定字符，默认空格

# strip()
str5 = '12jkjdk21'
print(str5.strip('12'))       # 截掉字符串头尾的指定字符，默认为空格

# maketrans()
# 创建字符映射的转换表
a = 'aeiou'
b = '12345'
c = str1.maketrans(a, b)
print(c)

# translate()
print(str1.translate(c))    # 按照转换表进行转换

# max()
print(max(a))           # 最大字符

# min()
print(min(a))           # 最小字符

# replace()
print(str1.replace('l', 'o', 2))  # 替换，不超过指定次数

# split()
print(str1.split(' '))         # 返回以某个字符分隔的后的列表

# splitlines()
str6 = 'dd\ndsdd\ndsd\n'
print(str6.splitlines())
print(str6.splitlines(True))   # 以行切片，默认不保留\n

# swapcase()
print(str1.swapcase())         # 进行字母的大小写转换

# title()
print(str1.title())            # 字符串中每个单词首字母大写

# zfill()
print(str1.zfill(20))          # 返回指定长度的字符串，不足前面补0

