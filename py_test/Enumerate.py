# -*- coding: utf-8 -*-
# Author: style_forever
# Date: 17
# Description: 莫烦python



# count = 0
# l = [11,22,33,44]
# for data in l:
#     if count == 2:
#         data += 11
#     l[count] = data
#     count += 1
# print(l)

# count = 0
# l = [11,22,33,44]
# for i in range(len(l)):
#     if count == 2:
#         l[i]+= 11
#     count += 1
# print(l)

#enumerate() 
#enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，
# 同时列出数据和数据下标，一般用在 for 循环当中。
# 语法格式如下：
# enumerate(iterable, start=0)
# 参数说明：
# iterable -- 一个可迭代对象，如列表、元组或字符串。
# start -- 下标起始位置，默认为 0。
# 返回值：
# 返回 enumerate(iterable, start) 函数返回一个 enumerate 对象，
# 其中包含两个元素：索引和对应的值。



l = [11,22,33,44]
for count, data in enumerate(l):
    if count == 2:
        data += 11
    l[count] = data
print(l)
