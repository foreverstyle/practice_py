# -*- coding: utf-8 -*-
# Author: style_forever
# Date: 13
# Description: 比较大小

# 输入两个数字，并比较大小

def compare_sizes(num1, num2):
    if num1 > num2:
        print(num1, "is greater than", num2)
    elif num1 < num2:
        print(num1, "is less than", num2)
    else:
        print(num1, "is equal to", num2)


# 测试
if __name__ == '__main__':
    compare_sizes(5, 10)
    compare_sizes(10, 5)
    compare_sizes(5, 5)