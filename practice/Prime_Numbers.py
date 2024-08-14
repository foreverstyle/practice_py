# -*- coding: utf-8 -*-
# Author: style_forever
# Date: 14
# Description: 质数判断

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

if __name__ == '__main__':
    while True:
        num = int(input("请输入一个数字："))
        if is_prime(num):
            print(num, "是质数")
        else:
            print(num, "不是质数")
