# -*- coding: utf-8 -*-
# Author: style_forever
# Date: 13
# Description: 交换变量

# python return 能返回多个值，可以用元组来接收

def exchange(a, b):
    a, b = b, a
    return a, b

if __name__ == '__main__':    
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    print("Before exchange: a = %d, b = %d" % (a, b))
    (a, b) = exchange(a, b)
    print("After exchange: a = %d, b = %d" % (a, b))