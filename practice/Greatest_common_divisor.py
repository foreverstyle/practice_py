# -*- coding: utf-8 -*-
# Author: style_forever
# Date: 14
# Description:最大公约数算法 

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

if __name__ == '__main__':
    a =int(input("请输入第一个数："))
    b =int(input("请输入第二个数："))
    print("最大公约数为：", gcd(a, b))