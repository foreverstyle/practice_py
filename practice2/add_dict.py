# -*- coding: utf-8 -*-
# Author: style_forever
# Date: 14
# Description: 合并字典

def add_dict(dict1, dict2):
    """
    合并两个字典
    :param dict1: 字典1
    :param dict2: 字典2
    :return: 合并后的字典
    """
    result = dict1.copy()
    result.update(dict2)
    return result


if __name__ == '__main__':
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'c': 3, 'd': 4}
    result = add_dict(dict1, dict2)
    print(result)

