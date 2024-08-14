# -*- coding: utf-8 -*-
# Author: style_forever
# Date: 14
# Description: 九九乘法表

for i in range(1, 10):
    for j in range(1, i+1):
        print(f"{i}*{j}={i*j}", end="\t")
    print()

