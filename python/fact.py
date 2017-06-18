#!/usr/bin/python3

def fact(n):
    if n <= 0:
        return
    if n==1:
        return 1
    return n * fact(n-1)

print(fact(0))
print(fact(1))
print(fact(100))
