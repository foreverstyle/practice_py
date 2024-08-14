# -*- coding: utf-8 -*-
# Author: style_forever
# Date: 14
# Description:约瑟夫环

def joseph_ring(n, k, m):
    """
    约瑟夫环
    :param n: 总人数
    :param k: 出局位置
    :param m: 循环次数
    """
    # 定义一个列表，用来保存剩余的人的编号
    people = list(range(1, n+1))
    # 循环 m 次
    for i in range(m):
        print('{}号出局了'.format(people.pop(k-1)))
        for j in range(k-1):
            people.append(people.pop(0))
    # 最后剩下的人是：
    print('最后剩下的人是：{}'.format(people))

if __name__ == '__main__':
    n = int(input('请输入总人数：'))
    k = int(input('请输入出局位置：'))
    m = int(input('请输入循环次数：'))
    joseph_ring(n, k, m)