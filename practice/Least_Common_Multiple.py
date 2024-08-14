# -*- coding: utf-8 -*-
# Author: style_forever
# Date: 14
# Description: 最小公倍数

import Greatest_common_divisor


def lcm(a, b):
    """
    计算两个数的最小公倍数
    :param a: 第一个数    
    :param b: 第二个数
    :return: 最小公倍数
    """
    return a * b // Greatest_common_divisor.gcd(a, b)


if __name__ == '__main__':
    a = int(input("请输入第一个数："))
    b = int(input("请输入第二个数："))
    print(lcm(a, b)) 