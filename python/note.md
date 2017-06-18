#廖雪峰python教程笔记
地址：http://www.liaoxuefeng.com

##0 python简介

python的定位:优雅,明确,简单.
python的缺点:运行速度慢,源代码必须公开.

python适合开发的应用类型：

- 网络应用：包括网站，后台服务等等
- 日常小工具：包括系统管理员需要的脚本任务等等
- 把其他语言开发的程序再包装起来，方便使用

用一种语言开始真正的开发软件时，除了编写代码以外，还需要很多基本的已经写好的现成的东西，来帮助你加快开发进度。高级编程语言通常都会提供一个比较完善的基础代码库,让你直接调用.
python为我们提供了非常完善的基础代码库,覆盖了网络,文件,GUI,数据库,文本等大量内容,被形象的称为"内置电池batteries included".
除了内置的库以外,python还有大量的第三方库.当然,如果你开发的代码通过很好的封装,也可以作为第三方库供别人直接使用.

##1.第一个Python程序

python中单、双引号等效

在Python交互式命令行下，可以直接输入代码，然后执行，并立刻得到结果。

- print():内置输出函数
- input():内置输入函数

```python
#!/usr/bin/python
# coding: utf-8

name = input('Please enter your name: ')
print('Hello!',name)
```
##2.Python基础

python的语法比较简单：基本就是冒号加缩进,文本编辑器中把tab统一设置成缩进4个空格。

```python
#!/usr/bin/python
# coding: utf-8
# print absolute value of an integer
a = 100
if a >= 0:
	print(a)
else:
	print(-a)
```

###2.1数据类型和变量

数据类型：

- 整数
	- 普通十进制和数学中的写法一样
	- 十六进制加0x前缀，比如：0xff00
- 浮点数：小数
	- 普通浮点数和数学中的写法一样
	- 数学中的科学计数法的写法：1.23e9, -3.4e8, 3.5e-9
- 字符串：就是用单引号或双引号括起来的任意文本
	- 单、双引号没有任何区别
	- \为转义字符：\n表示换行，\t表示制表符，\\表示\本身
	- 如果字符串内部有很多换行，python允许用'''...'''表示多行内容
	- r'...'默认引号内的内容都不转义
- 布尔值:与布尔代数表示完全一致，仅有True,False两种值,经常用在条件判断中。
	- 与，或，非的表示方法是：and, or, not
- 空值：用None表示，表示一个特殊的值。
- 列表：list, tuple
- 字典：dict, set
- 自定义数据类型

变量：
命名规则：英文大小写，数字和\_的组合，且不能用数字开头。
推荐：驼峰式有意义的描述

给一个变量赋值时，python解释器做了两件事：

- 在内存中创建了一个内容
- 在内存中创建了一个变量名，并把它指向刚才创建的内容

常量：所谓常量就是不能变的变量，通常用全部大写的变量名表示常量。
	事实上常量仍然是一个变量，python根本没有任何机制保证常量不会被改变。

关于除法：
10/3
3.3333333333
10//3
3
10%3
1

小结：
	python支持多种数据类型，在计算机内部可以把任何数据都看出一个“对象”。而变量就是程序中用来指向这些数据对象的，对变量赋值就是把数据和变量关联起来。
	注意：python的整数没有大小限制，但超出一定范围就直接表示为inf(无限大)

###2.2 字符串和编码

因为计算机在底层只能处理0和1的数字，如果要处理文本就必须先把文本转换为数字才能处理。早期用8个bit作为一个byte，一个byte最多能涵盖255种可能，对英文毫无问题，但对于汉语等非拼音语言来说就远远不够了。经过发展现在采用UTF-8的编码规则，既保证了可用性，又保证了经济性，同时兼顾向前兼容ASCII编码。

python中关于编码的两个内置函数：

- ord()--获取字符的十进制整数表示
- chr()--通过整数获取对应的字符

以Unicode表示的str通过encode()方法可以编码为指定的bytes，例如：

```
>>> 'ABC'.encode('ascii')
b'ABC'
>>> '中文'.encode('utf-8')
b'\xe4\xb8\xad\xe6\x96\x87'
>>> '中文'.encode('ascii')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)
```

反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法：

```
>>> b'ABC'.decode('ascii')
'ABC'
>>> b'ABC'.decode('utf-8')
'ABC'
>>> b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
'中文'
```

len()函数得到字符数，仔细体会下面的例子：

```
>>> len('ABC')
3
>>> len('中文')
2
>>> len(b'ABC')
3
>>> len(b'\xe4\xb8\xad\xe6\x96\x87')
6
>>> len('中文'.encode('utf-8'))
6
```

格式化输出：
在python中采用和C语言一致的方式，用%实现

占位符|表示整数
---:|---:
%d|整数
%f|浮点数
%s|字符串
%x|十六制整数

其中，格式化整数和浮点数还可以指定是否补0和整数与小数的位数：

```
>>> '%2d-%02d' % (3, 1)
' 3-01'
>>> '%.2f' % 3.1415926
'3.14'
```

如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串：

```
>>> 'Age: %s. Gender: %s' % (25, True)
'Age: 25. Gender: True'
```

有些时候，字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%：

```
>>> 'growth rate: %d %%' % 7
'growth rate: 7 %'
```

练习:

```python
#!/usr/bin/python3
#-*-coding:utf-8-*-
#格式化显示

'''
s1 = 72
s2 = 85
r = (s2 - s1)/s1*100
print('成绩增长了: %.1d%%' % r)
'''

#第二版

s1 = int(input('原来的成绩: '))
s2 = int(input('现在的成绩: '))
r = (s2 - s1)/s1*100
print('成绩增长了: %.1f%%' % r)
```

###2.3 使用list和tuple

####list:
列表,是一种有序集合,可以随时添加或删除元素,形式:

```
>>> classmates = ['Michael', 'Bob', 'Tracy']
>>> classmates
['Michael', 'Bob', 'Tracy']

#变量classmates就是一个list。用len()函数可以获得list元素的个数：
>>> len(classmates)
3
```

可以用索引访问list中每一个位置的元素,记得索引是从0开始的.所以最后一个元素的索引就是len(classmates) - 1.
另外一种表示逻辑:最后一个,classmates[-1],那么倒数第二个就是classmates[-2]...

list编辑函数:

- 末尾追加元素:classmates.append('Adam')
- 指定位置插入元素:classmates.insert(1,'Jack')
- 删除元素:classmates.pop(1).留空删除末尾元素
- 替换某个元素:classmates[1] = 'Sarah'

多维列表(数组):s = ['python', 'java', ['asp', 'php'], 'scheme']

####tuple:
另一种有序列表叫元组,tuple和list非常类似,但是tuple一旦初始化就不能修改,也没有append(),insert()等方法.
正因为tuple不可变,所以代码更安全.如果可能尽量用tuple代替list,形式:

```
>>>classmates = ('Michael', 'Bob', 'Tracy')
```

来看一个'可变的'tuple

```
>>> t = ('a', 'b', ['A', 'B'])
>>> t[2][0] = 'X'
>>> t[2][1] = 'Y'
>>> t
('a', 'b', ['X', 'Y'])
```

###2.4 条件判断
条件判断完整形式:

```
if <条件判断1>:
    <执行1>
elif <条件判断2>:
    <执行2>
elif <条件判断3>:
	<执行3>
else:
	<执行4>
```

if语句执行有个特点,它是从上往下判断,如果在某个判断上是True,把该判断对应的语句执行后,就忽略掉剩下的elif和else.所以要注意判断的先后顺序

练习

小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：

- 低于18.5：过轻
- 18.5-25：正常
- 25-28：过重
- 28-32：肥胖
- 高于32：严重肥胖

```python
#!/usr/bin/python3
#-*- coding: utf-8 -*-
#BMI test

h = float(input('Input your height(m): '))
w = float(input('Input your weight(kg): '))

bmi = w/(h*h)

if bmi < 18.5:
	print('过轻!')
elif bmi < 25:
	print('正常.')
elif bmi < 28:
	print('过重')
elif bmi < 32:
	print('肥胖!')
else:
	print('严重肥胖!!')
```

###2.5 循环
python中有两种循环:for x in...和while循环

####for...in...

依次把list或tuple中的每个元素迭代出来.

```
names = ['Michael', 'Bob', 'Tracy']
for name in names:
	print(name)
```

range(n)--内置函数,生成一个从0到n-1的整数序列

```
sum = 0
for x in range(101):
	sum = sum + x
print(sum)
```

####while
只要条件满足,就不断循环,条件不满足时退出循环.注意死循环!

```
sum = 0
n = 99
while n > 0:
	sum = sum + n
	n = n - 2
print(sum)
```

###2.6 使用dict和set

####dict
python内置的字典数据类型,类似其他语言的map,使用键-值(key-value)存储,具有极快的查找速度.形式:

```
>>> d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
>>> d['Micael']
95
```

把数据放入dict的方法，除了初始化时指定外，还可以通过key放入：

```
>>> d['Adam'] = 67
>>> d['Adam']
67
```

由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉：

```
>>> d['Jack'] = 90
>>> d['Jack']
90
>>> d['Jack'] = 88
>>> d['Jack']
88
```

如果key不存在，dict就会报错要避免key不存在的错误,有两种办法:

```
>>> 'Thomas' in d
False
>>> d.get('Thomas')
>>> d.get('Thomas', -1)
-1
```

要删除一个key,用pop(key)方法,对应的value也会从dict删除.

和list比较,dict有以下几个特点:

- 查找和插入的速度极快,不会随着key的增加而变慢.
- 需要占用大量的内存,内存浪费多.

而list相反:

- 查找和插入的时间随着元素的增加而增加.
- 占用空间小,浪费内存很少.

所以,dict是用空间来换取时间的一种方法.

####set
set和dict类似,也是一组key的集合,但不存储value.由于key不能重复,所以,在set中,没有重复的key.

```
>>> s = set([1,2,3])
>>> s
{1,2,3}
>>> s = set([1,1,2,3,4,4,4,4])
>>> s
{1,2,3,4}
#通过add(key)方法可以添加元素到set中,可以重复添加,但不会有效果.
>>> s.add(4)
{1,2,3,4}
#可以通过remove(key)方法删除元素
>>> s.remove(2)
>>> s
{1,3,4}
```

set可以看成数学意义上的无序和无重复元素的集合,因此,两个set可以做数学意义上的交集,并集等操作.

```
>>> s1 = set([1,2,3])
>>> s2 = set([2,3,4])
>>> s1 & s2
{2,3}
>>> s1 | s2
{1,2,3,4}
```

##3.函数

当代码出现有规律的重复的时候,就需要函数出场了.
借助抽象,我们才能不关心底层的具体计算过程,而直接在更高的层次上思考问题.

### 3.1 调用函数

python内置了很多有用的函数,我们可以直接调用.文档地址:
http://docs.python.org/3/library/functions.html
交互模式查看函数帮助help(functionName)

Buit-in Functions

|||Buit-in Functions|
---|---|---|---|---
abs()|dict()|help()|min()|setattr()
all()|dir()|hex()|next()|slice()
any()|divmod()|id()|object()|sorted()
ascii()|enumerate()|input()|oct()|staticmethod()
bin()|eval()|int()|open()|str()
bool()|exec()|isinstance()|ord()|sum()
bytearray()|filter()|issubclass()|pow()|super()
bytes()|float()|iter()|print()|tuple()
callable()|format()|len()|property()|type()
chr()|frozenset()|list()|range()|vars()
classmethod()|getattr()|locals()|repr()|zip()
compile()|globals()|map()|reversed()|\_\_import\_\_()
complex()|hasattr()|max()|round()|
delattr()|hash()|memoryview()|set()|

数据类型转换相关函数:int(),float(),str(),bool()

###3.2 定义函数

定义函数要使用def语句,依次写出函数名,括号,括号中的参数和冒号,然后在缩进块中编写函数体,函数的返回值用return语句返回.形式:

```python
def my_abs(x):
	#执行数据类型检查
	if not isinstance(x, (int, float)):
		raise TypeError('bad operand type')
	if x >= 0:
		return x
	else:
		return -x
```

如果你已经把my\_abs()的函数定义保存为abstest.py文件了,那么可以在该文件的当前目录下启动python解释器,用from abstest import my\_abs来导入my\_abs()函数,注意abstest是文件名,不包含.py扩展名.

小结:

- 定义函数时,需要确定函数名和参数个数;参数可以有默认值
- 如果有必要,可以先对参数的数据类型做检查
- 函数体内部可以用return随时返回函数结果
- 函数执行完毕也没有return语句时,自动return None
- 函数可以同时返回多个值,但其实就是一个tuple

定义一个空函数,用pass语句占位

```
def nop():
	pass
```

练习:定义一个函数quadratic(a,b,c),接收三个参数,返回一元二次方程的两个解.

```python
#!/usr/bin/python3
#解一元二次方程函数

import math
def quadratic(a,b,c):
	if not isinstance(a,(int,float) and (b,(int,float)) and (c,(int,float))):
		raise TypeError('bad operand type')

	s = (b*b) - (4*a*c) 	#尽量用括号区分计算优先顺序。
	if a == 0:
		x = -c/b
		return x
	elif s < 0:
		return 'No answer'
	elif s == 0:
		x = -b/(2*a)
		return x
	else:
		x1 = (-b + math.sqrt(s))/(2*a)
		x2 = (-b - math.sqrt(s))/(2*a)
		return (x1,x2)
```

小结:

- 定义函数时,需要确定函数名和参数个数
- 如果有必要,可以先对参数的数据类型做检查
- 如果有必要,可以先让参数有默认值,有默认值的参数要放在后面
- 函数体内部可以用return随时返回函数结果
- 函数执行完毕也没有return语句时,自动return None
- 函数可以同时返回多个值,但其实就是一个tuple.

###3.3 函数的参数

小结

Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。

默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！

要注意定义可变参数和关键字参数的语法：

*args是可变参数，args接收的是一个tuple；

\**kw是关键字参数，kw接收的是一个dict。

以及调用函数时如何传入可变参数和关键字参数的语法：

可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(\**{'a': 1, 'b': 2})。

使用\*args和\*\*kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。

定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。

###3.4 递归函数

如果一个函数在内部调用自身，这个函数就是递归函数.

##4.高级特性

##5.函数式编程

##6.模块

##7.面向对象编程

##8.面向对象高级编程

##9.错误、调试和测试

##10.IO编程

##11.进程和线程

##12.正则表达式

##13.常用内建模块

##14.常用第三方模块

##15.图形界面

##16.网络编程

##17.电子邮件

##18.访问数据库

##19.Web开发

##20.异步IO

##21.实战
