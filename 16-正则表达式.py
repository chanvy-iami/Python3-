# python3正则表达式
'''
正则表达式是一个特殊的字符序列，可检查一个字符串是否与某种模式匹配
re模块使python语言拥有全部正则表达式功能
compile函数根据模式字符串和可选的标志参数生成一个正则表达式对象
'''

# re.match()函数
'''
re.match()尝试从字符串的起始位置匹配一个模式
如果不是起始位置匹配成功
match()返回none

re.match(pattern, string, flags=0)
# pattern,匹配的正则表达式
# string,要匹配的字符串
# flags,标志位,用于控制正则表达式的匹配方式,如区分大小写、多行匹配等

可使用group(num)或group()匹配对象函数来获取匹配表达式
group(num=0)匹配的整个表达式的字符串
groups()返回一个包含所有小组字符串的元组
'''
import re
print(re.match('www', 'www.nowcoder.com'))
print(re.match('com', 'www.nowcoder.com'))

line = 'Cats are smarter than Dogs'
matchobj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
if matchobj:
    print(matchobj.group())
    print(matchobj.group(1))
    print(matchobj.group(2))
else:
    print('No match')

# . 匹配任意字符,除了换行符
# * 匹配0个或多个表达式
# ? 匹配0个或1个由前面正则表达式定义的片段
# () 匹配括号内的表达式,也表示一个组
# re.M 多行匹配 re.I 使匹配对大小写不敏感

# re.search()方法
'''
re.search扫描整个字符串并返回第一个成功的匹配
re.search(pattern, string, flags=0)
re.search方法返回一个匹配的对象,否则返回None
'''
print(re.search('www', 'www.nowcoder.com'))
print(re.search('com', 'www.nowcoder.com'))

# re.match与re.search的区别
'''
re.match只匹配字符串的开始
开始不符合正则表达式，则匹配失败，返回None
re.search匹配整个字符串,直到找到一个匹配
'''

matchobj1 = re.match(r'Dogs', line, re.M | re.I)
if matchobj1:
    print(matchobj1.group())
else:
    print('No match')
matchobj2 = re.search(r'Dogs', line, re.M | re.I)
if matchobj2:
    print(matchobj2.group())
else:
    print('No match')

# 检索和替换
'''
re.sub()用于替换字符串中的匹配项
re.sub(pattern, repl, string, count=0, flags=0)
pattern:正则中的模式字符串
repl:替换的字符串,也可为一个函数
string:要被查找替换的原始字符串
count:模式匹配后替换的最大次数,默认0表示替换所有匹配
flags:匹配模式,数字形式
'''
phone = '2004-959-559 # 这是一个电话号码'
num1 = re.sub(r'#.*$', '', phone)
print(num1)        # 删除注释
num2 = re.sub(r'\D', '', phone)
print(num2)        # 删除非数字

# $ 匹配字符串的末尾
# \D 匹配任意非数字

# repl参数是一个函数
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)
s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))

# \d 匹配任意数字
# + 匹配一个或多个表达式

# compile函数
'''
complie函数编译正则表达式，生成一个正则表达式（pattern）对象
供match()和search()两个函数使用
re.complie(pattern[, flags])
pattern:一个字符串形式的正则表达式
flags: 可选,表示匹配模式
'''
pattern = re.compile(r'\d+')
m1 = pattern.match('one12twothree34four')
print(m1)
m2 = pattern.match('one12twothree34four', 2, 10)
print(m2)
m3 = pattern.match('one12twothree34four', 3, 10)
print(m3)
print(m3.group())
print(m3.start())    # 子串第一个字符的索引
print(m3.end())      # 子串最后一个字符的索引+1
print(m3.span())

pattern1 = re.compile(r'([a-z]+) ([a-z]+)', re.I)
m4 = pattern1.match('Hello World Wide Web')
print(m4)
print(m4.group())
print(m4.span())
print(m4.group(1))
print(m4.span(1))
print(m4.group(2))
print(m4.span(2))
print(m4.groups())
# print(m4.group(3))

# findall()
'''
在字符串中找到正则表达式所匹配的所有子串
返回列表,如果没有找到,则返回空列表
# match和search是匹配一次,findall匹配所有
re.findall(string[, pos[, endpos]])
string:待匹配的字符串
pos:可选参数,指定字符串的起始位置,默认为0
endpos:可选参数,指定字符串的结束位置,默认为字符串长度
'''
pattern2 = re.compile(r'\d+')
res1 = pattern2.findall('nowcoder 123 google 456')
res2 = pattern2.findall('now88coder123google456', 0, 20)
print(res1)
print(res2)

# re.finditer()
'''
与findall类似,在字符串中找到正则表达式所匹配的所有子串,
并作为迭代器返回
re.finditer(pattern, string, flags=0)
'''
it = re.finditer(r'\d+', '12a32bc43jf3')
for match in it:
    print(match.group())

# re.split()
'''
spilt()方法按照能够匹配的子串将字符串分割后返回列表
re.split(pattern, string[, maxsplit=0, flags=0])
pattern:匹配的正则表达式
string:要匹配的字符串
maxsplit:分割次数
flags:标志位
'''
print(re.split('\W+', 'nowcoder, nowcoder, nowcoder.'))
print(re.split('(\W+)', ' nowcoder, nowcoder, nowcoder.'))
print(re.split('\W+', ' nowcoder, nowcoder, nowcoder.', 1))
print(re.split('a *', 'hello world'))

# \W+ 匹配非数字字母下划线

# 正则表达式对象
'''
re.RegexObject
re.compile()返回RegexObject对象
re.MatchObject
group()返回被RE匹配的字符串
'''

# 正则表达式修饰符-可选标志
'''
# re.I 使匹配对大小写不敏感
# re.L 做本地化识别匹配
# re.M 多行匹配
# re.S 使.匹配包括换行在内的所有字符
# re.U 根据Unicode字符集解析字符
# re.X 给予灵活格式使正则表达式写得更加易于理解
'''

# 正则表达式模式
'''
模式   描述
^	匹配字符串的开头
$	匹配字符串的末尾。
.	匹配任意字符，除了换行符，当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符。
[...]	用来表示一组字符,单独列出：[amk] 匹配 'a'，'m'或'k'
[^...]	不在[]中的字符：[^abc] 匹配除了a,b,c之外的字符。
re*	匹配0个或多个的表达式。
re+	匹配1个或多个的表达式。
re?	匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式
re{n}	匹配n个前面表达式。例如，"o{2}"不能匹配"Bob"中的"o"，但是能匹配"food"中的两个o。
re{n,}	精确匹配n个前面表达式。例如，"o{2,}"不能匹配"Bob"中的"o"，但能匹配"foooood"中的所有o。"o{1,}"等价于"o+"。"o{0,}"则等价于"o*"。
re{n, m}	匹配 n 到 m 次由前面的正则表达式定义的片段，贪婪方式
a|b	匹配a或b
(re)	匹配括号内的表达式，也表示一个组
(?imx)	正则表达式包含三种可选标志：i, m, 或 x 。只影响括号中的区域。
(?-imx)	正则表达式关闭 i, m, 或 x 可选标志。只影响括号中的区域。
(?: re)	类似 (...), 但是不表示一个组
(?imx: re)	在括号中使用i, m, 或 x 可选标志
(?-imx: re)	在括号中不使用i, m, 或 x 可选标志
(?#...)	注释.
(?= re)	前向肯定界定符。如果所含正则表达式，以 ... 表示，在当前位置成功匹配时成功，否则失败。但一旦所含表达式已经尝试，匹配引擎根本没有提高；模式的剩余部分还要尝试界定符的右边。
(?! re)	前向否定界定符。与肯定界定符相反；当所含表达式不能在字符串当前位置匹配时成功。
(?> re)	匹配的独立模式，省去回溯。

\A	匹配字符串开始
\Z	匹配字符串结束，如果是存在换行，只匹配到换行前的结束字符串。
\z	匹配字符串结束
\G	匹配最后匹配完成的位置。
\b	匹配一个单词边界，也就是指单词和空格间的位置。例如， 'er\b' 可以匹配"never" 中的 'er'，但不能匹配 "verb" 中的 'er'。
\B	匹配非单词边界。'er\B' 能匹配 "verb" 中的 'er'，但不能匹配 "never" 中的 'er'。
\n, \t, 等。	匹配一个换行符。匹配一个制表符, 等
\1...\9	匹配第n个分组的内容。
\10	匹配第n个分组的内容，如果它经匹配。否则指的是八进制字符码的表达式。
'''
# 字符类
'''
[aeiou]	匹配中括号内的任意一个字母
[0-9]	匹配任何数字。类似于 [0123456789]
[a-z]	匹配任何小写字母
[A-Z]	匹配任何大写字母
[a-zA-Z0-9]	匹配任何字母及数字
[^aeiou]	除了aeiou字母以外的所有字符
[^0-9]	匹配除了数字外的字符
'''

# 特殊字符类
'''
\w	匹配数字字母下划线
\W	匹配非数字字母下划线
\s	匹配任意空白字符，等价于 [\t\n\r\f]。
\S	匹配任意非空字符
\d	匹配任意数字，等价于 [0-9]。
\D	匹配任意非数字
'''
