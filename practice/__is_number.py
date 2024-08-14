# -*- coding: utf-8 -*-
# Author: style_forever
# Date: 13
# Description: 判断字符串是否为数字

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False 

if __name__ == '__main__':
    print(is_number('123'))
    print(is_number('123.456'))
    print(is_number('abc'))
    print(is_number('123a'))
    print(is_number(' '))
    print(is_number('我爱你'))