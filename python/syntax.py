#!/usr/bin/python
# -*-coding: utf-8-*-
# print absolute value of an integer.

'''
代码头一般采用上述格式
python的语法格式基本上就是简单的冒号+缩进，来组织代码块
'''

'''
b = input('Please enter an integer: ')
a = int(b)
#下面是等效的改版语句
'''
a = int(input('Please enter an integer: '))
if a >= 0:
    print(a)
else:
    print(-a)
