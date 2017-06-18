#!/usr/bin/python3
# -*- coding: utf-8 -*-
# for...in... and while loop.

sum = 0
for x in range(101):
    sum = sum + x
print('for...in... loop:')    
print('sum(100) =',sum) 

sum = 0
'''
n = 100
while n > 0:
    sum = sum + n
    n = n - 1   #特别注意的防止死循环
'''
n = 1
while n <= 100:
    sum = sum + n
    n = n + 1
print('while loop:')
print('sum(100) =',sum)
