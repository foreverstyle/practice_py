# -*- coding: utf-8 -*-
# Author: style_forever
# Date: 14
# Description: 求字典中所有值的和

def sum_dict(d):
    """
    求字典中所有值的和
    :param d: 字典
    :return: 字典中所有值的和
    """
    print(d.values())       #返回视图对象，([1, 2, 3]) ,可迭代对象 ,可使用sum()函数求和 
    return sum(d.values())
    

if __name__ == '__main__':
    d = {'a': 1, 'b': 2, 'c': 3}
    print(sum_dict(d))

