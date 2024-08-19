# -*- coding: utf-8 -*-
# Author: style_forever
# Date: 17
# Description: 莫烦python

name = ["a", "b", "c"]
score = [1,2,3]
d = {}
for i in range(3):
    d[name[i]] = score[i]
print(d)

name = ["a", "b", "c"]
score = [1,2,3]
d = {}
for n, s in zip(name, score):
    d[n]=s
print(d)