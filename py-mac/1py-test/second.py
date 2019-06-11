# -*- coding: UTF-8 -*-
from collections import Iterable
import os

# 函数相关
print('--------------- "内置函数 - start"----------------')
print(abs(-1))  # 绝对值
print(cmp(2, 1))  # 类似java的compareTo   大于返回1，小于返回-1，等于返回0
# 数据类型转换
print(int('123'))
print(int(12.34))  # 向下取整
print(float('12.34'))
print(str(12.34))
print(bool(1))  # true
print(bool(0))  # true
print(bool(''))  # false
print(bool('avc'))  # true
# 函数名只是一个函数对象的引用
a = abs
print(a(-1))
# 函数定义,函数定义上下空两行
print('--------------- "内置函数 - end"----------------')
print

print('--------------- "自定义函数 异常处理 - start"----------------')
def my_abs(x):
    "进行参数校验"    #函数首行注释
    if not isinstance(x, (int, float)):
        raise TypeError('你还不给老子赶忙输入数字！！！')  #抛出异常,自定义异常信息
    if x > 0:
        return  # 意思是return none
    else:
        return 'brew'
#try:... except *Error:... else:...
try:
    print(my_abs('a'))
except TypeError, error:    #追加获得异常信息,BaseException是所有异常的基类
    print error;
except:     #异常只会被捕获一次
    print "抓住了异常"
else:
    print "没有异常发生时 会执行lse"
finally:
    print "finally code...."
# print(my_abs('abc'))
if 5 > 6:
    pass  # pass意味着什么都不做，跟continue没关系
print('--------------- "自定义函数 异常处理 - start"----------------')
print

# 返回多值时实际上返回的是一个元组
# 参数默认值必须放在后面，通过默认参数值的设置，提高方法的调用简易型
print('--------------- "自定义函数[必备参数、默认参数、关键字参数] - start"----------------')
def enroll(name, gender, age=10, address='北京'):
    print '**********'
    print 'name:', name
    print 'gender', gender
    print 'age', age
    print 'address', address
    print '**********'

enroll('abc', 'man', 12, '南京')
enroll('aa', 'women')
enroll('aaaaaa', 1234, address='上海')    #关键字参数必须放在必备参数后面
print('--------------- "自定义函数[必备参数、默认参数、关键字参数] - end"----------------')
print

print('--------------- "自定义函数[默认参数 陷阱] - start"----------------')
def add_test(L=[]):
    "函数默认值陷阱：py函数并不是每次调用的时候初始化，而是在编辑阶段只初始化一次。以后每次调用都是指向原来的函数对象"
#暂时只在"可变对象"默认值的情况下发现了该陷阱
    L.append('END')
    return L

print(add_test())
print(add_test())

# 默认值方式，使得每次调用该方法L都会被指向None,当调用者两次调用都传入参数时也没关系，因为每次调用L都被重新指向了None
def add_end(L=None):
    if L is None:
        L = []
    L.append('end')
    return L
print(add_end([1, 2, 3]))
print(add_end([1, 2, 3]))
print('--------------- "自定义函数[默认参数 陷阱] - end"----------------')
print

print('--------------- "自定义函数[不定长参数] - start"----------------')
print


def calc(*numbers):
    "*代表接受一个元组;"
    sum = 0
    for num in numbers:
        sum = sum + num
    return sum


# 两种传递可变参数的方式
print(calc(1, 2, 3))
lsittest = [1, 3, 4]
print(calc(*lsittest))


def person(name, age, **other):
    "**代表接受一个字典dic"
    print('name', name, 'age', age, 'other', other)
    abc = other.get('address')
    print(abc)
    if abc is not None:
        print(abc.decode('utf-8'))
    print(other.get('gender'))


person('zhangsan', 12)
# 关键字参数，实际上是一个dict
person('lissi', 13, address='北京', gender='women')
dicttest = {'address': '北京', 'gender': 'women'}
person('wangwu', 14, **dicttest)    #同可变参数一样，调用时都需要额外加* 或 **
#参数定义/传递顺序：必选参数，默认参数，可变参数，关键字参数


def func(a, b, c=0, *agrs, **kw):
    print('a=', a, 'b=', b, 'c=', c, 'args=', agrs, 'kw=', kw)


L = [1, 2, 3, 4]
LL = {'sid': 'bre'}
func(*L, **LL)  #任何函数都可以通过这种方式调用
print('--------------- "自定义函数[不定长参数] - end"----------------')
print
print('--------------- "函数作用域[globel] - end"----------------')
a = 1


def aaa():
    global a
    a = a +1
    return a


print aaa()
print('--------------- "函数作用域[globel] - end"----------------')
print

print('--------------- "匿名函数 - start"----------------')
sum = lambda arg1, arg2: arg1 + arg2
print "arg1 + arg2 等于：", sum(1, 2)
print('--------------- "匿名函数 - end"----------------')
print


def funTest(a):
    if a is not 1:
        return
    print a


print funTest(2)    #无反回值的return 返回 None

def fact(n):
    "py递归"
    if n == 1:
        return 1
    return n+fact(n-1)


print('digui 500 result:', fact(500))    #传入1000会导致栈溢出。每调用一次，加一层栈帧，函数每返回一次，就减一次栈帧；


print '--------------- "list/tuple sub操作 - start"----------------'
r = [1, 2, 3, 4]
print(r[0:3])   #切片操作，同样是包头不包尾
print(r[-2:])   #倒叙切片，取倒数第1个、倒数第二个，两个元素
print('abc'[0:1])
print((1, 2, 3)[0:1])
print((1, 2, 3)[0:2])
print '--------------- "list/tuple sub操作 - end"----------------'
print

print '--------------- "list/string/dic 迭代操作 - start"----------------'
r = [1, 2, 3, 4]
dicttest2 = {'dicA': 1, 'dicB': 2}
for key in dicttest2:   #迭代dic的key，无序。同Map
    print(key)
    print(dicttest2.get(key))

for value in dicttest2.itervalues():    #迭代dict的value
    print(value)

for item in dicttest2.iteritems():
    print(item)

for ch in 'abcdefg':
    print(ch)
print '--------------- "list/string/dic 迭代操作 - end"----------------'
print

print '--------------- "isinstance/range/enumerate函数使用。 list/tuple 生成器 - start"----------------'
print range(2, 10, 2)   #range(start, end, step)
print(isinstance(123, Iterable))    #需要 from collections import Iterable
print(isinstance('abc', Iterable))
#如果遍历list并且每次都想拿到下标，可以这么操作：
r = [3, 4, 5]
for i in enumerate(r, 1):  #枚举 list 之后，会得到一个由duple组成的list。每一个duple第一个元素的list的角标，第二个元素是list的value
    print i
    print i[1]
print "---"
# or
for i in range(len(r)):
    print i
    print r[i]
print "---"

LLL = []
for i in range(1, 11):  #range(start, end) -> [start, ... ,end-1]
    LLL.append(i * i)
print(LLL)
print "---"

print([num * num for num in range(1, 11)])  #列表生成器
print([m + n for m in 'ABC' for n in 'XYZ'])    #双重并列循环，生成全排列
print [d for d in os.listdir('.')]     #输出os模块.目录即当前目录下的所有entity

Ltest = ['abc', 12, 'dEF']
print([i.lower() for i in Ltest if isinstance(i, str)])     #加判断的列表生成器.str/list/int 都输入关键字
#生成器学习
LLtest = (num for num in range(10)) #获得的是该tuple的迭代器
print(LLtest.next())
print(LLtest.next())
print(LLtest.next())
print "-----"
for num in LLtest:  #可以直接遍历迭代器。但其起始位置可能已经发生了变化。
    print(num)
print '--------------- "isinstance/range/enumerate函数使用。 list/tuple 生成器 - end"----------------'
print

print "进阶系列........ 不想看系列..."


def fib(max):       #斐波拉契数列 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a+b   #可以理解为a、b都是同时读入，等都计算完之后，再往回写
        print('verify:', a, b)
        n = n + 1


print('--------------')
#fib(10)


def fib2(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b         #使用yield关键字变成1个generator
        a, b = b, a+b
        n = n + 1


print(fib2(10))


def odd():      #这是1个generator 每次next会在执行到yield时退出，下次执行从上次退出的地方继续执行
    print('step 1')
    yield 1
    print('step 3')
    yield 3
    print ('step 5')
    yield 5


o = odd()
print(o.next())
print(o.next())
print(o.next())