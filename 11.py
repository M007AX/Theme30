for n in range(0, 100):
    if (n*(n-1)*4 + (n - 1)**2) >= 1000:
        print(n)
"""
from turtle import *
n = 3
speed(0) #самая быстрая {'fastest':0, 'fast':10, 'normal':6, 'slow':3, 'slowest':1 } см. исходную библиотеку
for i in range(4):
    forward(n*40)
    right(90)
    forward(n*40)
    left(90)
    forward(n*40)
    right(90)
penup()
for x in range(-10, 10):
    for y in range(-10, 10):
        setpos(x*40, y*40)
        dot(4, 'red')
x = input()
"""
