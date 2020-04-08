# close()方法

'''
用于关闭一个已打开的文件，关闭后的文件不能再进行读写操作
close()方法允许调用多次
fileobject.close()
无返回值
'''

# 打开文件
fo = open('test.txt', 'wb')
print('文件名:', fo.name)
# 关闭文件
fo.close()


# flush()方法

'''
flush()方法用来刷新缓冲区，即将缓冲区中的数据立刻写入文件
同时清空缓冲区，一般文件关闭会自动刷新，但有时关闭前需要刷新
fileobject.flush()
无返回值
'''

# 打开文件
fo = open('test.txt', 'wb')
print('文件名:', fo.name)
# 刷新缓冲区
fo.flush()
# 关闭文件
fo.close()


# fileno()方法

'''
fileno()方法返回一个整性的文件描述符
fileobject.fileno()
返回文件描述符
'''

# 打开文件
fo = open('test.txt', 'wb')
print('文件名:', fo.name)
fid = fo.fileno()
print('文件描述符:', fid)
# 关闭文件
fo.close()


# isatty()方法

'''
isatty()方法检测文件是否连接到一个终端设备
fileobject.isatty()
返回bool类型
'''

# 打开文件
fo = open('test.txt', 'wb')
print('文件名:', fo.name)
ret = fo.isatty()
print('返回值:', ret)
# 关闭文件
fo.close()


# read()方法

'''
read()方法用于从文件读取指定的字节数，未指定则读取所有
fileobject.read()
返回字符串的字节
'''

# 打开文件
fo = open('test1.txt', 'r+')
print('文件名:', fo.name)
line = fo.read(2)
print('读取字符串: %s' % (line))
# 关闭文件
fo.close()


# readline()方法

'''
readline()方法读取从文件读取整行(包括换行符)，指定参数读取固定字节
fileobject.readline()
返回读取的字符串
'''

# 打开文件
fo = open('test1.txt', 'r+')
print('文件名:', fo.name)
line = fo.readline()
print('读取第一行:%s' % (line))
lineh = fo.readline(3)
print('读取第一行:%s' % (lineh))
# 关闭文件
fo.close()


# readlines()方法

'''
readlines()方法用于读取所有行，并返回列表
fileobject.readlines()
'''

# 打开文件
fo = open('test1.txt', 'r+')
print('文件名:', fo.name)
for line in fo.readlines():
    line = line.strip()
    print('读取的数据:%s' % (line))
# 关闭文件
fo.close()


# seek()方法

'''
seek()方法用于移动文件读取指针到指定位置
fileobject.seek(offset, whence)
offset为开始偏移量
whence默认为0，从文件开头算起，1从当前位置，2从文件末尾
'''

# 打开文件
fo = open('test1.txt', 'r+')
print('文件名:', fo.name)
line = fo.readline()
print('读取字符串: %s' % (line))
fo.seek(9)
line2 = fo.readline()
print('读取字符串: %s' % (line2))
# 关闭文件
fo.close()


# tell()方法

'''
tell()方法返回文件的当前位置，即文件指针的当前位置
fileobject.tell()
'''

# 打开文件
fo = open('test1.txt', 'r+')
print('文件名:', fo.name)
line = fo.readline()
print('读取字符串: %s' % (line))
# 获取当前文件位置
pos = fo.tell()
print('当前位置: %d' % (pos))
# 关闭文件
fo.close()


# truncate()方法

'''
truncate()方法用于从文件首行首字节开始截断
可指定截断的字节数，截断后面的字节被删除
fileobject.turncate()
无返回值
'''

# 打开文件
fo = open('test1.txt', 'r+')
print('文件名:', fo.name)
# 截取字节数
fo.truncate(5)
str1 = fo.read()
print('截取: %s' % (str1))
# 关闭文件
fo.close()


# write()方法

'''
write()方法向文件中写入指定字符串
fileobject.write()
返回写入字符串的长度
'''

# 打开文件
fo = open('test1.txt', 'r+')
print('文件名:', fo.name)
# 文件末尾写入
fo.seek(0, 2)
fo.write('1235sd')
fo.seek(0, 0)
for line in fo.readlines():
    line = line.strip()
    print('读取的数据:%s' % (line))
# 关闭文件
fo.close()


# writelines()方法

'''
writelines()方法向文件中写入一序列字符串
fileobject.writelines()
无返回值
'''

# 打开文件
fo = open('test1.txt', 'r+')
print('文件名:', fo.name)
# 文件多行写入
fo.writelines(['hhdhhdh\n', 'hdsihi989'])
# 关闭文件
fo.close()