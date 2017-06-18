#!/usr/bin/python3
# -*- coding: utf-8 -*-
# BMI

h = float(input('输入你的身高(m): ')) 
w = float(input('输入你的体重(kg)'))

bmi = w/(h*h)

if bmi < 18.5:
    print('过轻!')
elif bmi < 25:
    print('正常.')
elif bmi < 28:
    print('过重.')
elif bmi < 32:
    print('肥胖!')
else:
    print('严重肥胖!!')
