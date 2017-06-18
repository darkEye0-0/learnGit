#!/usr/bin/python3
#-*- coding: utf-8 -*-
# 一元二次方程函数定义练习

import math
def quadratic(a,b,c):
    if not isinstance(a,(int,float)) and (b,(int,float)) and (c,(int,float)):
        raise TypeError('bad operand type')

    s = (b*b) - (4*a*c)
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
