# 迭代器

'''
迭代是访问集合的一种方式
迭代器可以记住遍历位置的的对象
迭代器对象从集合的第一个元素开始访问，直到所有元素被访问完结束
迭代器只能往前不能后退
'''

a = [1, 5, 2, 6]    # 用列表对象创建迭代器
b = iter(a)
print(next(b))      # 迭代器的两个基本方法，iter()和next()
print(next(b))
for x in b:
    print(x, end=' ')  # 迭代器对象可通过for循环进行遍历

print('----')

# 创建一个迭代器

'''
将一个类作为一个迭代器需要在类中实现两个方法
iter()和next()
'''

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        y = self.a
        self.a += 1
        return y

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))

print('----')

# StopIteration

'''
StopIteration异常用于标识迭代的完成，防止出现无限循环的情况
可在next()方法中设置指定循环次数后触发StopIteration异常结束迭代
'''

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 10:
            y = self.a
            self.a += 1
            return y
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)

# 生成器

'''
使用yield的函数称为生成器
生成器是一个返回迭代器的函数，只能用于迭代操作
调用生成器的过程中，遇到yield函数会暂停并保存当前运行信息，
返回yield的值，并在下次执行next()方法从当前位置继续执行
调用生成器函数返回一个迭代器对象
'''