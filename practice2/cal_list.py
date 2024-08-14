# -*- coding: utf-8 -*-
# Author: style_forever
# Date: 14
# Description: 计算列表和，计算列表积

from functools import reduce
def cal_list_add(lst):
    return reduce(lambda x,y:x+y,lst)

def cal_list_mul(lst):
    return reduce(lambda x,y:x*y,lst)


if __name__ == '__main__':
    lst = [1,2,3,4,5]
    print(cal_list_add(lst))
    print(cal_list_mul(lst))